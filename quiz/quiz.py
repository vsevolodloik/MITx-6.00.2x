# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:25:04 2017

@author: Vsevolod Loik
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    if songs[0][2] > max_size:
        return []
    else:
        playlist = [songs[0][0]]
        sizeRemaining = max_size - songs[0][2]
        songs.pop(0)
        songsSorted = sorted(songs, key=lambda x: x[2], reverse = False)
        for i in songsSorted:
            if sizeRemaining >= i[2]:
                playlist.append(i[0])
                sizeRemaining -= i[2]
            else:
                return playlist
    return playlist
        
  
songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
song_playlist(songs, 12.2)




def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    maxContigSum = 0
    for i in range(0, len(L)):
        for j in range(i+1, len(L)+1):     
            if sum(L[i:j]) > maxContigSum:
                maxContigSum = sum(L[i:j])
    return maxContigSum
    
    
    
def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION
    posGuess = 0
    negGuess = 0
    while True:    
        if test(posGuess) == False:
            posGuess += 1
        else: 
            return posGuess
        if test(negGuess) == False:
            negGuess -= 1
        else: 
            return negGuess
            
    

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))

def f(x):
    return x+5 == 3
print(solveit(f))