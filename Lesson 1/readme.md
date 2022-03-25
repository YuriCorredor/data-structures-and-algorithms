<h1>Binary Search, Linked Lists and Complexity</h1>

<h3>Linear search:</h3>
<p>In computer science, a linear search or sequential search is a method for finding an element within a list. It sequentially checks each element of the list until a match is found or the whole list has been searched.</p>

<h3>Binary search:</h3>
<p>Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.</p>

<h2>Question:</h2>
<p>Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.</p>

<h2>Systematic strategy for solving problems:</h2>
<p>1. State the problem clearly. Identify the input & output formats.</p>
<p>2. Come up with some example inputs & outputs. Try to cover all edge cases.</p>
<p>3. Come up with a correct solution for the problem. State it in plain English.</p>
<p>4. Implement the solution and test it using example inputs. Fix bugs, if any.</p>
<p>5. Analyze the algorithm's complexity and identify inefficiencies, if any.</p>
<p>6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.</p>

<h2>Tests</h2>
<p>Before we start implementing the function, it is useful to come up with some example inputs and outputs which we can use later to test out problem.</p>
<p>Edge Cases: It's likely that you didn't think of all cases when you read the problem for the first time. Some of these (like empty array or query not occurring in cards) are called edge cases, as they represent rare or extreme examples.</p>
<p>While edge cases may not occur frequently, your programs should be able to handle all edge cases, otherwise they may fail in unexpected ways. All test cases for this specific problem is listed on tests.py.</p>

<h2>Brute Force</h2>
<p>Our first goal should always be to come up with a correct solution to the problem, which may necessarily be the most efficient solution. The simplest or most obvious solution to a problem, which generally involves checking all possible answers is called the brute force solution.</p>
<p>Always try to express (speak or write) the algorithm in your own words before you start coding. It can be as brief or detailed as you require it to be. Writing is a great tool for thinking clearly. It's likely that you will find some parts of the solution difficult to express, which suggests that you are probably unable to think about it clearly. The more clearly you are able to express your thoughts, the easier it will be for you to turn into code.</p>
<p>In a real interview or coding assessment, you can skip the step of implementing and testing the brute force solution in the interest of time. It's generally quite easy to figure out the complexity of the brute for solution from the plain English description.</p>

<h2>Algorithm's complexity</h2>
<h3>Complexity and Big O Notation</h3>
<p>Complexity of an algorithm is a measure of the amount of time and/or space required by an algorithm for an input of a given size e.g. N. Unless otherwise stated, the term complexity always refers to the worst-case complexity (i.e. the highest possible time/space taken by the program/algorithm to process an input).</p>
<p>Big O Notation: Worst-case complexity is often expressed using the Big O notation. In the Big O, we drop fixed constants and lower powers of variables to capture the trend of relationship between the size of the input and the complexity of the algorithm i.e. if the complexity of the algorithm is cN^3 + dN^2 + eN + f, in the Big O notation it is expressed as O(N^3)</p>

<h2>Apply the right technique to overcome the inefficiency</h2>
<p>The next best idea would be to pick a random card, and use the fact that the list is sorted, to determine whether the target card lies to the left or right of it. In fact, if we pick the middle card, we can reduce the number of additional cards to be tested to half the size of the list. Then, we can simply repeat the process with each half. This technique is called binary search.</p>

<h2>Problems for Practice</h2>
Binary Search Problems on LeetCode: https://leetcode.com/problems/binary-search/