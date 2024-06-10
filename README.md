# Chatbot using NLTK

This is a simple chatbot project built using Python and NLTK library. The chatbot is capable of engaging in conversation with users based on predefined patterns and responses. The algorithm used in this project, which relies on regular expressions for pattern matching and NLTK for preprocessing, is a fundamental and widely-used approach in natural language processing and chatbot development.

<div style="display: inline">
    <img src="https://img.icons8.com/color/48/000000/python.png" alt="Python" width="32" height="32"/>
    <img src="https://miro.medium.com/v2/resize:fit:1184/format:webp/1*YM2HXc7f4v02pZBEO8h-qw.png" alt="NLTK" width="32" height="32"/>
    <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg" alt="Jupyter Notebook" width="32" height="32"/>
    <img src="https://www.opc-router.com/wp-content/uploads/2023/12/icon_json-datei_format_1200-1-800x320.png" alt="JSON File" width="50" height="32"/>
    <img src="https://img.icons8.com/color/48/000000/git.png" alt="Git" width="32" height="32"/>
    <img src="https://img.icons8.com/color/48/000000/linux.png" alt="Linux" width="32" height="32"/>
    <img src="https://img.icons8.com/color/48/000000/console.png" alt="Bash" width="32" height="32"/>
</div>



## Installation

1. Make sure you have Python installed on your system.
2. Install NLTK library using pip:
    ```
    pip install nltk
    ```

## Usage

1. Clone or download the repository.

```
git clone https://github.com/niladrridas/chatbot
```

2. Navigate to the project directory.
3. Run the `test1.ipynb` or `test1.py` script.

```
jupyter notebook test1.ipynb
```
or
```
python test1.py
```


4. You can interact with the chatbot by typing your messages in the terminal, debugging it in your machine or running [Jupyter Notebook](https://jupyter.org/) server in using [PyCharm](https://www.jetbrains.com/pycharm/), [Visual Studio Code](https://code.visualstudio.com/) or much more [IDEs](https://aws.amazon.com/what-is/ide/#:~:text=An%20integrated%20development%20environment%20(IDE,easy%2Dto%2Duse%20application.)).

## Features

- Responds to greetings like "hello", "hi", "hey".
- Introduces itself when asked for its name.
- Responds positively to user's emotions like happiness, excitement, etc.
- Handles queries about its age, the weather, sports/games, and current world leaders.
- Allows adding new patterns and responses dynamically.
- Read ideas from [reference](/docs/REFERENCE.md).

## Adding New Patterns and Responses

You can easily extend the chatbot's capabilities by adding new patterns and responses. Use the `add_pattern()` function in the scripts to do so.

```
add_pattern(r"(.*)", ["Custom response"])
```

## Communication Flow Diagram

```
sequenceDiagram
    participant User
    participant Chatbot

    User ->> Chatbot: "Hello"
    Chatbot ->> User: "Hello"
    User ->> Chatbot: "What is your name?"
    Chatbot ->> User: "I'm a bot. I'm called Part-time Bot."
    User ->> Chatbot: "I'm feeling happy today"
    Chatbot ->> User: "That's great to hear"
    User ->> Chatbot: "quit"
    Chatbot ->> User: "Bye. It was nice talking to you. See you soon :)"
```

## Journals:

1. [ACM Transactions on Interactive Intelligent Systems (TiiS)](https://dl.acm.org/journal/tiis)
2. [Journal of Artificial Intelligence Research (JAIR)](https://www.jair.org/index.php/jair)
3. [IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)](https://www.computer.org/csdl/journal/tp)
4. [Natural Language Engineering (NLE)](https://www.cambridge.org/core/journals/natural-language-engineering)
5. [Journal of Machine Learning Research (JMLR)](https://www.jmlr.org/)
6. [Computational Linguistics (CL)](https://www.mitpressjournals.org/loi/coli)
7. [ACM Transactions on Speech and Language Processing (TSLP)](https://dl.acm.org/journal/tslp)
8. [Information Retrieval Journal](https://www.springer.com/journal/10791)
9. [Expert Systems with Applications](https://www.journals.elsevier.com/expert-systems-with-applications)

## Conferences:

1. [Conference on Empirical Methods in Natural Language Processing (EMNLP)](https://www.aclweb.org/anthology/events/emnlp-2021/)
2. [Annual Meeting of the Association for Computational Linguistics (ACL)](https://www.aclweb.org/anthology/2021.acl-main/)
3. [International Conference on Computational Linguistics (COLING)](https://coling2022.org/)
4. [International Conference on Intelligent User Interfaces (IUI)](https://iui.acm.org/)
5. [Conference on Human Factors in Computing Systems (CHI)](https://chi2022.acm.org/)
6. [International Conference on Web Search and Data Mining (WSDM)](https://www.wsdm-conference.org/2022/)
7. [International Conference on Language Resources and Evaluation (LREC)](https://lrec2022.lrec-conf.org/)
8. [Conference on Conversational User Interfaces (CUI)](https://cui.acm.org/2021/)
9. [International Conference on Artificial Intelligence (IJCAI)](https://ijcai.org/)
10. [Conference on Information and Knowledge Management (CIKM)](https://www.cikm2022.org/)

## License

[MIT License](/LICENSE)