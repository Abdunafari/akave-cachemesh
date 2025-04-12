# Akave CacheMesh

🚀 Akave CacheMesh is a decentralized hot retrieval layer for AI models and datasets.

🧱 Built using:
- Rust (for high-speed caching microservice)
- Python FastAPI (frontend orchestrator)
- Akave SDK (planned integration)

## Use Case
Accelerate loading of data from fileCoin via Akave to be used in Web3 dApps, Decentralised AI Agents, blockchain solution by caching frequently accessed files to reduce cost spent in accessing date in decentralised storage.

## Structure
- `rust_cache/`: Rust Actix-web LRU cache microservice
- `python_frontend/`: FastAPI app that calls Rust backend and fetches model from AkaveSDK
- React for UI 
- `storage/`: Simulated decentralized files

## To Run

### Rust Backend:
```bash
cd rust_cache
cargo run
