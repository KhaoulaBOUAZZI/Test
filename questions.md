# Questions

## Question 1

Fill in the two functions `compute_histogram_bins` and `plot_histogram` in `histogram.py`. As an example, we would like to be able to plot something similar to histogram_example.png` as a minimum result.

## Question 2

Go to the file `question2.py`:
1. fill in `send_data_to_backend` so that it returns the list of the peer's connection durations.
2. fill in `process_backend_data` which must do all necessary processing to return the connection durations histogram bins counts. **Don't call `plot_histogram` in this method, we just want to compute the histogram bins counts**.

## Question 3

With peers sending such datastructure and our _backend_ server making such operations, we retrieve exactly **all** the connection durations on the network at the moment of the snapshot and we are able to plot the _exact distribution_ of the connection durations.
1. `question2.py` main has several simulations with increasing numbers of peers and peer pool size. Run the simulations with your implementation. What do you see? Can you explain the limitations of the implementations of question 2 taking into account that a _real_ peer network can have _millions_ of peers? (answer below in this file)
>> _answer here_
As we can notice, for a fixed number of max_peer_pool_size, the time taken by the backend is higher when the number_of_peers is higher. However this starts to be more remarkable and causes a noticeable difference in the time measure when the number of peers gets higher and higher. Taking into consideration that number_of_peers can reach millions this will highly increase the time difference which will be unbearable and heavy calculation. Besides, for a given number_of_peers , the higher the max_peer_pool_size gets the higher the time taken by the backend gets which is kind of logical because the more peers connect between theem the more the total connexion duration increases.
## Question 4

Go to the file `question4.py`:
1. propose new implementations of `send_data_to_backend` and `process_backend_data` that can deal with millions of peers _and_ still provide a good representation of the _distribution_ of the connection duration. You are free to add any written comments, add pictures etc...to enhance your answer.
>> _answer here_

As we can see in the calculation of the duration of a peer's peer_pool coonexion, we are supposing that a peer reaches always and necessarily its maximum number of connexion. It means that : supposing for example that a peer has at maximum max_peer_pool_size=10 , this doesn't mean that it will connect to them at the same time and moment so it's not logical to add all durations together because for each peer2peer relation there's a certain probability that this peer will connect to other which was not considered previously. Therefore, when implementing the method send_data_to_backend we shouldn't consider all the connections'durations.
For the process_backend_data, I could't unfortuanetely think about another implementation that can optimize the code