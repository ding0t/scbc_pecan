---
tags:
    - lesson
    - forensics
---

# 11 AI

1. Generative AI
1. [AI ethics](#ai-ethics)
1. Intro to AI pair programming
1. awareness of  different AI coding tools

## Generative AI

The creation of new content using AI. The AI model collates all the information it can access, and produces a aggregated new content from that data.

This is great for most things, but AI will get things wrong, and will miss out on deeper expertise. So it is best suited to simpler tasks, and where a problem has an answer that is absolute.

## AI ethics

🧠 _Some AI usage and ethics to apply_

1. Use AI for approprate tasks
    1. Maintain control of major decision making
    1. Does explainability matter for your applciation?
1. Maintain critical thinking
    1. Can you verify correctness of the content
    1. Use the generated content to learn
1. Acknowledge use of a generative AI tool
1. Be aware of the age of the data the AI was trained on - e.g. ChatGPT 3.5 was trained 2 years ago.
1. Be aware of AI hallicination - the AI can collate information in a way that generates false information, both deliberately and accidentaly. The AI does not understand the content it generates.
    * Example of when this [matters](https://www.bbc.com/news/world-us-canada-65735769)


# Using AI for programming

AI is a useful tool but be aware it does get things wrong. It is trained on public data, and some of this data is inaccurate. 


## Pair programming with AI

We can program with generative AI using chat to ask for a program function to give a starting point. 

To do this effectively:

1. Keep the problems relatively simple and discrete

Alterantively, as we code the AI can do interactive code completion. Within a interactive development environment, like Microsoft Visual Studio Code, the AI will read your code, and develop boilerplate code suggestions.

To do this effectively:
1. Write clear comments that explain the intent of your code - the AI reads these like a person would
1. Review all code suggestions - make sure you understand the code it has suggested, and test its output is as expected
1. Use to fast prototype - this fits CTFs really well


## Generative AI platform options

There are many - the below are a couple you can try without having to sign up.

* [ChatGPT on the web](https://chat.openai.com/) Fast and generally ok results.
* [Copilot on the web](https://copilot.microsoft.com/) Results a little slow, but not too bad


# Test it out

Use the Pecan love letter challenge [love letter](https://pecanplus.ecusdf.org/?page=challenges&challenge=loveletter)

We already know how we want to solve it

```
write a python program to take the list of numbers:  [315, 324, 363, 294, 294, 363], divide each number in the list by three, then print the corresponding ascii value of each number as a string
```


# References

* [Ai assistance for pair programming](https://stackoverflow.blog/2024/04/03/developers-with-ai-assistants-need-to-follow-the-pair-programming-model/)