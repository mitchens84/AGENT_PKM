:::mermaid
graph TD
    User((User)) <--> TelegramBot[Telegram Bot Interface]
    TelegramBot --> |Text Query| Main[src/main.py]
    TelegramBot --> |Voice Message| Main
    Main --> DataUtils[src/utils/data_utils.py]
    DataUtils --> |Transcription| AssemblyAI[AssemblyAI API]
    Main --> PKMAgent[src/agents/pkm_agent.py]
    PKMAgent <--> ResearchWorkflow[src/workflows/research_workflow.py]
    ResearchWorkflow --> NotionService[src/services/notion_service.py]
    ResearchWorkflow --> AirtableService[src/services/airtable_service.py]
    ResearchWorkflow --> VectorStore[src/components/memory.py]
    VectorStore --> Pinecone[Pinecone API]
    NotionService --> Notion[Notion API]
    AirtableService --> Airtable[Airtable API]
    ResearchWorkflow --> StateManager[src/state/state_manager.py]
    PKMAgent --> LanguageModel[OpenAI GPT]
    
    classDef component fill:#f9f,stroke:#333,stroke-width:2px;
    classDef external fill:#bbf,stroke:#333,stroke-width:2px;
    class Main,PKMAgent,ResearchWorkflow,NotionService,AirtableService,VectorStore,DataUtils,StateManager component;
    class AssemblyAI,Pinecone,Notion,Airtable,LanguageModel external;
    
    subgraph Legend
        ComponentNode[Internal Component]
        ExternalService[External Service/API]
        class ComponentNode component;
        class ExternalService external;
    end
:::