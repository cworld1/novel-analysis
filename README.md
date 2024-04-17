# Novel Analysis

<!-- [![GitHub stars](https://img.shields.io/github/stars/cworld1/novel-analysis?style=flat-square)](https://github.com/cworld1/novel-analysis/stargazers)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cworld1/novel-analysis?label=commits&style=flat-square)](https://github.com/cworld1/novel-analysis/commits)
[![GitHub license](https://img.shields.io/github/license/cworld1/novel-analysis?style=flat-square)](https://github.com/cworld1/novel-analysis/blob/main/LICENSE) -->

A simple project for analyzing Chinese novels. All data is crawled from [红袖读书](https://www.hongxiu.com/)

## Main technology stack

- Python: Flask, Pyecharts, statsmodels
- Node.js: Bun, Vite, React, Ant Design
- Database: Json, CSV
<!-- - Rust: Pyo3 -->

## Project Structure

- `anal`: Analysis scripts
- `data`: Data directory
- `crawl`: Crawler scripts
- `fetch`: Basic info for api scripts
- `web`: Frontend dashboard

## Data Constructed

Data can be crawled from the script in the following steps. After running the crawler script, the data will be saved in the `data` directory.

The repository [Novel Data](https://github.com/cworld1/novel-data) also contains the data, which has been a submodule part of this project.

## Local Development

Clone the repository:

```shell
git clone https://github.com/cworld1/novel-analysis.git
# If you wang to also get data, you can also clone the submodule
# git clone https://github.com/cworld1/novel-analysis.git --recurse-submodules
cd novel-analysis
```

### Crawl & Analysis Server

Environment requirements:

- [Python](https://www.python.org/downloads/): 3.8+

1. Create a virtual environment:

   ```shell
   python -m venv .venv
   source .venv/bin/activate
   ```

   Or you can use tools for your own:

   - [virtualenv](https://virtualenv.pypa.io/en/latest/)
   - [pipenv](https://pipenv.pypa.io/en/latest/)
   - [poetry](https://python-poetry.org/)
   - [conda](https://docs.conda.io/en/latest/)
   - [uv](https://github.com/astral-sh/uv/)

2. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Run crawler script (if needed)

   ```shell
   python ./crawl/main.py
   ```

4. Run the server script

   ```shell
   python ./api.py
   # or run: python -m flask --app ./api.py run
   ```

### Display Dashboard

Environment requirements:

- [Nodejs](https://nodejs.org/): 18.0.0+
- [Bun](https://bunjs.dev/): 1.0.0+

2. Install dependencies:

   ```shell
   bun install
   ```

3. Start the development server:

   ```shell
   bun dev
   ```

   This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

4. Some useful commands:

   - `bun build`: Bundles the app into static files for production.
   - `bun lint`: Lints the project for potential errors.
   - `bun preview`: Preview the production build locally.

## Contributions

To spend more time coding and less time fiddling with whitespace, this project uses code conventions and styles to encourage consistency. Code with a consistent style is easier (and less error-prone!) to review, maintain, and understand.

### Be consistent

If the style guide is not explicit about a particular situation, the cardinal rule is to **be consistent**. For example, take a look at the surrounding code and follow its lead, or look for similar cases elsewhere in the codebase.

### Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules:

- Configure the top-level `parserOptions` property like this:

```js
export default {
  // other rules...
  parserOptions: {
    ecmaVersion: "latest",
    sourceType: "module",
    project: ["./tsconfig.json", "./tsconfig.node.json"],
    tsconfigRootDir: __dirname,
  },
};
```

- Replace `plugin:@typescript-eslint/recommended` to `plugin:@typescript-eslint/recommended-type-checked` or `plugin:@typescript-eslint/strict-type-checked`
- Optionally add `plugin:@typescript-eslint/stylistic-type-checked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and add `plugin:react/recommended` & `plugin:react/jsx-runtime` to the `extends` list

## Thanks

- [红袖读书](https://www.hongxiu.com/)
- [文心中文心理分析系统 (Text Mind)](http://ccpl.psych.ac.cn/textmind/)
- [Jieba](https://github.com/fxsjy/jieba/)

## License

This project is licensed under the GPL 3.0 License.
