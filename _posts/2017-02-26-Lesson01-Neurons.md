# Lesson 01 - Neurons
## AKA - "What the frickity frackity hickity heckity is a neuron?"

![Earnest says "Yeah, my Neural Network uses a 3 dimensional input neuron vector, so what-". There is a list on a screen showing numbers 1,2, and 3. Ann asks Earnest "You mean that?"](http://img.hoff.in/learnest/svg/learnest0.svg)

## It's easier than you think

People in the machine learning industry love to throw around the word neuron.
And why shouldn't they? It's a great word. It brings to mind images of futuristic AIs that can think,
complicated neuroscience, and auspicious discoveries.

However, the use of it in machine learning is not only deceptive, but redundant. Machine learning documentation can often make more sense if you just remove the word neuron entirely.

For example:
"I'm feeding in two 3-dimensional input neurons"

Can easily become:
"I'm feeding in two 3-dimensional inputs"

(Of course this isn't always the case, but for the purposes of this introduction, and begginer level machine learning, it will be helpful to think of it in that way)


## You don't need 3-D glasses

Now let's look at the dimensions of the neuron.

One of my biggest gripes with beginner level machine learning tutorials is how they usually don't explain what they mean by phrases like `784 dimensional vector space` (I'm looking at you, tensorflow MNIST tutorial). A lot of the time, it's actually fairly simple. Let's take our comic from the beginning of the post as an example. 

In the first panel, our protagonist (Dubbed L'earneast by the artist, J. Hoff), describes his `3 dimensional input neuron vector`. 

Remove the word neuron and it's just a 3 dimensional input vector, which looks like this:
```python
[
  [1],
  [2],
  [3]
]
```
So now we have a vector with a shape of (3, 1). And since we just have one value for each "dimension" of the array, we can just flatten it into a stanard list.

```python
[1,2,3]
```
And there you have it, a 3 dimensional input neuron. 
