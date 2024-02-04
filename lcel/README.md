# LangChain Expression Language

## streaming

when execute the file [streaming](./streaming.py), it panic:

```shell
(langchain310) PS D:\workspace\llm\langchain\lcel> python .\streaming.py
Sure!| I'm a highly advanced language model that can perform a wide range of tasks, including language understanding, language generation, and even generating images based on|Traceback (most recent call last):
  File "D:\workspace\llm\langchain\lcel\streaming.py", line 26, in <module>
    loop.run_until_complete(streamodel())
  File "D:\programdata\conda\envs\langchain310\lib\asyncio\base_events.py", line 649, in run_until_complete
    return future.result()
  File "D:\workspace\llm\langchain\lcel\streaming.py", line 20, in streamodel
    async for s in model.astream("Hi, tell me something about yourself."):
  File "D:\programdata\conda\envs\langchain310\lib\site-packages\langchain_core\language_models\chat_models.py", line 307, in astream
    raise e
  File "D:\programdata\conda\envs\langchain310\lib\site-packages\langchain_core\language_models\chat_models.py", line 298, in astream
    generation += chunk
  File "D:\programdata\conda\envs\langchain310\lib\site-packages\langchain_core\outputs\chat_generation.py", line 57, in __add__
    generation_info = merge_dicts(
  File "D:\programdata\conda\envs\langchain310\lib\site-packages\langchain_core\utils\_merge.py", line 40, in merge_dicts
    raise TypeError(
TypeError: Additional kwargs key created already exists in left dict and value has unsupported type <class 'int'>.
```

it's a bug of langchain, wait be fixed, but we can change the code 
%CONDA_HOME%/envs/langchain310/lib/site-packages/langchain_core/utils/_merge.py

from:
```python
def merge_dicts(left: Dict[str, Any], right: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dicts, handling specific scenarios where a key exists in both
    dictionaries but has a value of None in 'left'. In such cases, the method uses the
    value from 'right' for that key in the merged dictionary.

    Example:
        If left = {"function_call": {"arguments": None}} and
        right = {"function_call": {"arguments": "{\n"}}
        then, after merging, for the key "function_call",
        the value from 'right' is used,
        resulting in merged = {"function_call": {"arguments": "{\n"}}.
    """
    merged = left.copy()
    for k, v in right.items():
        if k not in merged:
            merged[k] = v
        elif merged[k] is None and v:
            merged[k] = v
        elif v is None:
            continue
        elif merged[k] == v:
            continue
        elif type(merged[k]) != type(v):
            raise TypeError(
                f'additional_kwargs["{k}"] already exists in this message,'
                " but with a different type."
            )
        elif isinstance(merged[k], str):
            merged[k] += v
        elif isinstance(merged[k], dict):
            merged[k] = merge_dicts(merged[k], v)
        elif isinstance(merged[k], list):
            merged[k] = merged[k] + v
        else:
            raise TypeError(
                f"Additional kwargs key {k} already exists in left dict and value has "
                f"unsupported type {type(merged[k])}."
            )
    return merged
```

to:

```python
def merge_dicts(left: Dict[str, Any], right: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dicts, handling specific scenarios where a key exists in both
    dictionaries but has a value of None in 'left'. In such cases, the method uses the
    value from 'right' for that key in the merged dictionary.

    Example:
        If left = {"function_call": {"arguments": None}} and
        right = {"function_call": {"arguments": "{\n"}}
        then, after merging, for the key "function_call",
        the value from 'right' is used,
        resulting in merged = {"function_call": {"arguments": "{\n"}}.
    """
    merged={"input_tokens": 530, "output_tokens":2, "totoal_tokens":532}
    return merged

```
