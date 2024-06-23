# docstringai
Python scripts to generate doc strings using AI.

Command:

```bash
docker run --rm -it -v ollama:/root/.ollama -p 11434:11434 -v $PWD:/data/ -v /Users/bhag/.ollama/models/:/root/.ollama/models/ --entrypoint bash --name ollama docstringai
```
