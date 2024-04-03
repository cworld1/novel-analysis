# Novel Analysis

<!-- [![GitHub stars](https://img.shields.io/github/stars/cworld1/novel-analysis?style=flat-square)](https://github.com/cworld1/novel-analysis/stargazers)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cworld1/novel-analysis?label=commits&style=flat-square)](https://github.com/cworld1/novel-analysis/commits)
[![GitHub license](https://img.shields.io/github/license/cworld1/novel-analysis?style=flat-square)](https://github.com/cworld1/novel-analysis/blob/main/LICENSE) -->

## Local Development

Environment requirements:

- [Python](https://www.python.org/downloads/): 3.8+

1. Clone the repository:

   ```shell
   git clone https://github.com/cworld1/novel-analysis.git
   cd novel-analysis
   ```

2. Create a virtual environment:

   ```shell
   python -m venv .venv
   source .venv/bin/activate
   ```

   Or you can use tools for your own:

   - [virtualenv](https://virtualenv.pypa.io/en/latest/)
   - [pipenv](https://pipenv.pypa.io/en/latest/)
   - [poetry](https://python-poetry.org/)
   - [conda](https://docs.conda.io/en/latest/)
   - [uv](https://github.com/astral-sh/uv)

3. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

### Run crawler script

```shell
python ./crawl/main.py
```

## Contributions

To spend more time coding and less time fiddling with whitespace, this project uses code conventions and styles to encourage consistency. Code with a consistent style is easier (and less error-prone!) to review, maintain, and understand.

### Be consistent

If the style guide is not explicit about a particular situation, the cardinal rule is to **be consistent**. For example, take a look at the surrounding code and follow its lead, or look for similar cases elsewhere in the codebase.

## Thanks

- [文心中文心理分析系统 (Text Mind)](http://ccpl.psych.ac.cn/textmind/)
- [Jieba](https://github.com/fxsjy/jieba)

## License

This project is licensed under the GPL 3.0 License.
