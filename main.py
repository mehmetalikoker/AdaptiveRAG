from dotenv import load_dotenv
from graph.graph import app

load_dotenv()


if __name__ == '__main__':
    print(app.invoke(input={"question": "What is rag concept?"}))
    #app.get_graph().draw_mermaid_png(output_file_path="graph_architecture.png")

