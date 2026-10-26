from dotenv import load_dotenv
import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


def main():
    try:
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')

        # Load configuration settings
        load_dotenv()

        foundry_endpoint = os.getenv("FOUNDRY_ENDPOINT")
        agent_name = os.getenv("AGENT_NAME")

        # Create project client
        project_client = AIProjectClient(
            endpoint=foundry_endpoint,
            credential=DefaultAzureCredential(),
        )

        # Get OpenAI client
        openai_client = project_client.get_openai_client()

        # Get user prompt
        prompt = input("User prompt: ")

        # Send request to agent
        response = openai_client.responses.create(
            input=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            extra_body={
                "agent_reference": {
                    "name": agent_name,
                    "type": "agent_reference"
                }
            },
        )

        print(f"\n{agent_name}:")
        print(response.output_text)

    except Exception as ex:
        print(f"Error: {ex}")


if __name__ == "__main__":
    main()	