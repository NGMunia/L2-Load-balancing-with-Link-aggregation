# L2-Load-balancing-with-Link-aggregation

Spanning Tree Protocol (STP):

- The selected spanning tree protocol is Rapid Spanning Tree Protocol (RSTP).
- Switch SW2 has been designated as the root bridge for both VLANs 10 and 20.

Load Balancing:

- For effective load balancing, VLAN 10 traffic directed towards SW1 through the following intermediary switches: SW5, SW3, SW2.
- Similarly, VLAN 20 traffic aimed at SW2 takes a deliberate path through the switches: SW5, SW4, SW2.



Link Aggregation:

Link aggregation involves grouping multiple physical links, often between switches, into a single logical channel or port channel.

The configuration process includes selecting the ports to be aggregated, specifying the aggregation mode (active/passive or active/active for LACP or desirable/desirable or desirable/auto for PagP), and enabling the appropriate aggregation protocol.

Link aggregation allows multiple physical links to act as a single logical link, effectively increasing the overall bandwidth available between connected devices.

If one link fails, traffic can be automatically rerouted through the remaining operational links, enhancing network availability.

Traffic can be distributed across the aggregated links, preventing bottlenecks and ensuring efficient utilization of available bandwidth.

Aggregated links are usually given a virtual interface, often referred to as an "EtherChannel" or "Port-Channel," which is assigned an IP address if it's used for Layer 3 purposes.


- Layer 2 Link Aggregation Control Protocol (LACP) configuration is employed for the aggregation of links among SW2, SW3, and SW5.
- The link aggregation connecting SW2, SW4, and SW5 is established using Layer 2 Port Aggregation Protocol (PAgP).
- A Layer 3 Link Aggregation Control Protocol (LACP) arrangement is set up between switches SW1 and SW2, enhancing both bandwidth and redundancy.




Verification:

Verification procedures are carried out through the utilization of GET requests.

The act of querying the system for information is performed using HTTP GET requests.

APIs have been configured to handle and process GET requests for  the following specific types of information.
- EtherChannels Summary API:
   - This API is structured to respond to GET requests seeking information regarding EtherChannels. 
   - It provides a summarized overview of the EtherChannels setup in the network.

- VLANs API:
   - The VLANs API has been configured to handle incoming GET requests aimed at acquiring details about the various VLANs existing within the network.

- Spanning-Tree Instance API for Specific VLAN:
   - This API has been designed to cater to GET requests that inquire about the specifics of the  spanning-tree instance associated with a particular VLAN. 

