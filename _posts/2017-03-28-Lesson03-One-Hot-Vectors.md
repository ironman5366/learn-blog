---
authors:
    - beddow
---

# Lesson 03 - One Hot Vectors

## Classification models

One of the most important and most common type of problems in machine learning is that of classification.

Classification resolves around the idea that you have a lot of data and need to know what it is.

For example, say I want to sort my library of Linus Torvalds pictures.

I have two types of pictures.

Happy Linus:
![](https://ironmn5366.github.io/learn-blog/_assets/happylinus.jpg)

And angry Linus:

![](https://ironmn5366.github.io/learn-blog/_assets/angrylinus.png)

Easy enough, right?

For our input, we just need to convert an image to a vector using a library like opencv2, and then for the training data attach a binary label.

Let's say 0 for happy, and 1 for angry.

That would leave us with something like this:

|Picture|Output|
|---------------------------------------------------------|---|
|![](https://ironmn5366.github.io/learn-blog/_assets/happylinus.jpg)|`0`|
|![](https://ironmn5366.github.io/learn-blog/_assets/angrylinus.png)|`1`|

Simple enough, right?

I would add in a `sigmoid` activation to my keras model  (that's where the output is always between 0 and 1), use some of their handy binary classification tools, and then bam, I'm done.

But what if Linus gets another emotion? That leads us into the main use case for one hot vectors:

## Multi class classification

Let's say one day, when doing my daily Linus image search, I find a new emotion.

![](https://ironmn5366.github.io/learn-blog/_assets/excitedlinus.jpg)

Like any self respecting Linux fan, I take my library of Linus Torvalds pictures incredibly seriously.
I knew this would make a fine addition to my collection, but it didn't fit in either of my existing categories.

We need a new one.

Let's call it `excited`.

Now that we have more than two classes, we can't use binary classification any more. So what should we do?

That's where one-hot vectors come in.

One hot vectors have one "hot" quantity, that's 1, and the rest are 0. You can think of them like a table.

For our new model, we'll need three "classes". Happy, angry and excited.

For a picture that's happy, happy will be 1, and angry and excited will both be 0.

Let's take a look

|Picture|Happy|Angry|Excited|
|-------|-----|-----|-------|
|![]((https://ironmn5366.github.io/learn-blog/_assets/happylinus.jpg)|`1`|`0`|`0`|
|![](https://ironmn5366.github.io/learn-blog/_assets/angrylinus.png)|`0`|`1`|`0`|
|![](https://ironmn5366.github.io/learn-blog/_assets/excitedlinus.jpg)|`0`|`0`|`1`|

And there we go!

That's all for now folks and remember, keep your CPUs cool and your vectors hot. Check back in a few days for our next article, which will give you a workable example of a classification model.
