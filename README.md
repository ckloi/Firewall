### Testing

I created an unit test script to test all the negative cases for each rule. (if more time permited, i will cover positive cases)


### Interesting coding, design, or algorithmic choices

At first, I thought about storing all the possible ip address and port number in hash table, so that it guarantee O(1) for accepting packet. However, it sacrefies a huge amount of space. It may take up to O(2^32) space complexity to do so. Thus, I choose to use two array of rules there may not be too much of rules in firewall in real world. Then, I split rules into two part: tcp rules and udp rules because I belived they both share approximately same frequency, so whenever a new packet arrive, it should be check against its protocol rule. 

### optimizations if more time permited 

If more time permited, I would spend more time on researching graph representation of decision making. I may switch to build a policy making database that support quick query on incomming packet.

### Team that I'm interested

1. Platform team
2. Data team
3. Policy team
