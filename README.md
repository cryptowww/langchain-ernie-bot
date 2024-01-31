# LangChain example using ERNIE-Bot  

## Prepare

```shell

pip install langchain

pip install qianfan

```

## How to Save the API key safely

I use dynaconf package with toml to archive the safety object.

```shell
pip install dynaconf

# then, in the project directory

dynaconf init -f toml
```

save the api key in .secret.toml


