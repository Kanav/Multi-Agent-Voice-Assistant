"""
Build and compile the LangGraph StateGraph.

Graph topology:

  START → orchestrator ─┬─ product_agent ──→ synthesizer → END
                        └─ support_agent ──↗

Each agent is internally a subgraph with a model ⇄ tools loop.
The MemorySaver checkpointer persists conversation history across
turns, enabling multi-turn HITL (agent asks a question on one turn,
user answers on the next).
"""

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from src.config import get_logger
from src.nodes import orchestrator_node, product_agent, support_agent, synthesizer_node
from src.state import CartState
from IPython.display import display, Image

logger = get_logger("graph")


def build_graph() -> StateGraph:
    """Create, wire, and compile the Cart multi-agent graph."""

    builder = StateGraph(CartState)

    # ── Add nodes ────────────────────────────────────────
    builder.add_node("orchestrator", orchestrator_node)
    builder.add_node("product_agent", product_agent)
    builder.add_node("support_agent", support_agent)
    builder.add_node("synthesizer", synthesizer_node)

    # ── Add edges ────────────────────────────────────────
    builder.add_edge(START, "orchestrator")
    builder.add_edge("synthesizer", END)

    # ── Compile with checkpointer ────────────────────────
    # MemorySaver persists graph state so that interrupt()-based
    # HITL can pause and resume, and conversation history carries
    # forward between queries.
    memory = MemorySaver()
    graph = builder.compile(checkpointer=memory)

    logger.info("Graph compiled  (with MemorySaver for conversation persistence)")
    return graph


# Module-level singleton
cart_graph = build_graph()

if __name__ == "__main__":
    # Generate the PNG data
    png_data = cart_graph.get_graph().draw_mermaid_png()

    # Save it to a file
    with open("graph.png", "wb") as f:
        f.write(png_data)

    # Optionally display it in a notebook
    display(Image(filename="graph.png"))