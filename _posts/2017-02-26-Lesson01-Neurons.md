---
authors:
    - beddow
    - hoffer
---
# Lesson 01 - Neurons
## AKA - "What the frickity frackity hickity heckity is a neuron?"

[![Earnest says "Yeah, my Neural Network uses a 3 dimensional input neuron vector, so what-". There is a list on a screen showing numbers 1,2, and 3. Ann asks Earnest "You mean that?"][comic0]][comic0]

$$
\textrm{Ann shows L'earnest that his} \\
\textrm{ neurons aren't so impressive.}
$$

- [Neural networks don't have neurons][0]
	- We say 'inputs' and 'outputs' — not neurons
- [Neural networks don't need vectors][1]
	- [Vectors explained with memes][1.0]
	- [Let's just call vectors lists][1.1]

[0]: #neural-networks-dont-have-neurons
## Neural networks don't have neurons

People in the machine learning industry love to throw around the word neuron.

And why shouldn't they? It's a great word. It brings to mind discoveries in neuroscience and _futuristic AI_ that can think and feel. _However,_ the use of it in machine learning is redundant. Neural network documentation makes more sense if you remove the word neuron entirely.

- For example:
	- "I'm feeding in two 3-dimensional input neurons"
- Can easily become:
	- "I'm feeding in two 3-dimensional inputs"

(This applies to general purpose machine learning - not for models of neurons)

[1]: #neural-networks-dont-need-vectors
## Neural networks don't need vectors

[![Line says "Hi- I'm a line, i.e. a 1-dimensional vector-space!" The line goes from Ok at 0 to Spooky at 4. Line asks self "..but which memes are the freshest?" after seeing Salt Bae and Badger are both Ok at 0 and Skeleton is Spooky at 4. The line becomes a square, and line says "I'm now a square, i.e. a 2-dimensional vector-space". Salt Bae is Ok and Fresh at 0,17. Badger is Ok and Stale at 0,3. Skeleton is Spooky and somewhat fresh as 4,12.][comic1]][comic1]

$$
\textrm{A line can measure spookiness,} \\
\textrm{ but one must master the square} \\
\textrm{ to list spookiness and freshness.}
$$

Now let's look at the _dimensions_ of the inputs.

In many entry-level machine learning tutorials, they usually don't explain what they mean by a  `N-dimensional vector space` (I'm looking at you, [tensorflow "beginner" tutorial](https://www.tensorflow.org/get_started/mnist/beginners)). It's simple. 

As in the spooky-fresh comic above, think of a `vector space` as a shape. An `N-dimensional` vector space is just a __line__ for `N=1`, a __square__ for `N=2`, a _cube_ for `N=3`, or a _hypecube_ for `N>3`. It's best never to speak of _hypecubes_. Let's focus on __lines__ and __squares__.

[1.0]: #vectors-explained-with-memes
### Vectors explained with memes

A `vector` is a `list` _of directions in a space_.
- In the case of a __line__ _(1-dimensional space)_
	- A `vector` like `[4]` is offset from `[0]` by:
		- four steps along the line from zero.
- For a __square__ _(2-dimensional space)_
	- A `vector` like `[4,12]` is offset from `[0,0]` by
		- four steps along the first edge.
		- twelve steps along the second edge.

__Examples from [the spooky-fresh comic][1]:__
- A spooky line _(1-dimensional spooky space)_:
	- The ![spooky][spooky] `vector [4]` goes to __four__ steps of _spookiness_.
	- Both ![cute][cute] and ![salt][salt] `vectors [0]` stay at __zero__ _spookiness_. 
- A spooky-fresh square _(2-dimensional spooky-fresh space)_:
	- The ![spooky][spooky] `vector [4, 12]` goes `4` and `12` steps from `[0,0]`: 
		-  it goes to a _very spooky_ __four__ steps of _spookiness_.
		-  it goes to a _somewhat fresh_ __twelve__ steps of _freshness_.
	- While ![cute][cute] and ![salt][salt] still stay at __zero__  _spookiness_,
		- ![cute][cute] `vector [0,3]`  _(from 2003)_ only goes to __three__ steps of  _freshness_.
		- ![salt][salt] `vector [0,17]` _(from 2017)_ goes to __seventeen__ steps of _freshness_.

__Which memes are the freshest:__

To know anything about _freshness_, one item in your _input list_ must be a number for freshness. It's not needed to think of an `input vector` as offsetting an input in a space, but that's where the language of _vectors_ and _dimensions_ originates. __In general__, you need to list one item in the __input list__ for each feature like _spookiness_, _freshness_, or even _spiciness_.
- Notice that there is no difference between ![cute][cute] and ![salt][salt] if your inputs only list steps towards _spookiness_. Neither of those memes is spooky at all! 
- In _spooky-fresh_ space, our inputs are `[0,3]` for ![cute][cute] and `[0,17]` for ![salt][salt],
	-  so an artificial neural network can learn that that ![salt][salt] is _much fresher_ than ![cute][cute].

[comic0]: http://img.hoff.in/learnest/png/learnest0.png
[comic1]: http://img.hoff.in/learnest/png/dimensions.png
[spooky]: http://img.hoff.in/learnest/icons/0_spooky0.png
[salt]: http://img.hoff.in/learnest/icons/0_ok1.png
[cute]: http://img.hoff.in/learnest/icons/0_ok0.png


[1.1]: #lets-just-call-vectors-lists
### Let's just call vectors lists

In the [first panel][0], L'earnest describes his `3 dimensional input neuron vector`.

From what we learned about vectors, the inputs are a list of steps in a 3d space (a cube). But there's no cube in the code. When running a network, a `3 dimensional vector` would just be a `list with three items` like this:
```
input = [1,2,3]
```
If this is a `spooky-fresh-spicy` cube, the above input list could mean `spookiness=1`, `freshness=2`, and `spiciness=3`. 

Or, since the ![spooky][spooky] meme has `spookiness=4`, `freshness=12`, and `spiciness=0`,

```
input = [4,12,0]
```

There is no need to use a word like `dimensional` to talk about the inputs you feed into your neural network. 

__Helpful Translations:__

- L'earnest would say:
	- "I'm feeding in two 3-dimensional input neurons."
	- "I need another dimension to represent my input vector."
- He should have said:
	- "I'm feeding in two inputs of 3-item lists."
	- "I need to list another number for each input."
