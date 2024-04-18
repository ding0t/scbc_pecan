# Objectives

1. intro to ai pair programming
1. what is an ai coding vs ml
1. awareness of  different ai coding tools
1.

# Using AI for programming

AI is a useful tool but be aware it does get things wrong. It is trained on public code, and some of this code is inaccurate. In some tests, AI generally performed a bit better than the average first year university programming students. [ref]()

## AI ethics

🧠 _Some AI usage and ethics to think about_

1. Use AI for approprate tasks
    1. Maintain control of major decision making
    1. Does explainability matter for your applciation?
1. Maintain critical thinking
    1. Can you verify correctness of the content
    1. Use the generated content to learn
1. Acknowledge use of a generative AI tool
1. Be aware of AI hallicination - the AI can collate information in a way that generates false information, both deliberately and accidentaly. The AI does not understand the content it generates.


## Generative AI

The creation of new content using AI


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