# Ticket-Selling Platform Load Balancing and Data Consistency System

## Overview

This repository contains the code and configuration files for implementing a load balancing system and ensuring data consistency across servers for a ticket-selling platform. The system is designed to handle surges in traffic during ticket releases while maintaining a seamless user experience and preventing server overload and data inconsistency issues.

## Components

### Load Balancing System

The load balancing system consists of the following components:

1. **Load Balancer**: Directs incoming traffic across multiple server instances based on least connections algorithm.
2. **Server Instances**: Multiple server instances are deployed to handle incoming requests. These instances are configured identically and can scale horizontally based on traffic patterns.

### Data Consistency
we chose to use **strong consistency**.

To ensure data consistency across servers, we need to implement the following components:

1. **Database update**: if we are not changing the database we should update the database synchronicly.But if we can change the database so that each event data is in seperated file, then we can use asynchronous update but just for different files(events).
2. **Distributed Locks**: Manages concurrent writes using distributed locks to maintain data integrity across database update.
If the database remain unchanged we lock the database each time we enter the sell ticket function. If we changes the database to seperated events, each event data in different file, we lock the specific file, this way we allow concurent tickets selling for different events.
 
### upsides and downsides:
Synchronous Update:
Upsides: Immediate consistency, straightforward implementation.
Downsides: Potential performance bottleneck due to locking entire database, limited scalability for concurrent transactions.

Asynchronous Update (Event-based):
Upsides: Improved scalability with concurrent updates for different events, reduced contention.
Downsides: Eventual consistency, complexity in managing distributed locks, potential for conflicts during concurrent updates.

Global Lock (Database level):
Upsides: Ensures consistency by preventing concurrent writes, simple to implement.
Downsides: Reduced concurrency, potential for contention and performance issues under heavy load.
 
## Work team
Aya abbas + Maysa Zbidat
we worked together during the zoom meeting by sharing the screen and disccusing and thinking together,
and each one pushed her code to github. 


