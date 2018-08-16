# Unbounding a function from its functionality with state oracles

In order to achieve maximu flexibility in decentralization, we need states that do not depend on any particular dapp or platform. We need unbounded states. This means that any state can always be processed by any software. In return we get a variety of possible solutions to the situation.

However, we loose some important functionalities with unbounding states from applications. For instance, applications work as controllers that guarantee proper order of states during multi-hop state transitions. Applications also have methods that conduct a transition from one state to another (e.g. business logic in a model).

With state oracles we can manage a transition and keep proper order of unbounded states. State oracles are small programs that guarantee a proper transition from one state to another (e.g. from a product to its order). Similar to current development patterns (e.g. MVC), some of oracles may manage the change of a view, some can act as controllers and some can conduct transitions that resemble a business logic.

![State Oracles General Scheme](/docs/images/so-general-scheme.png?raw=true "State Oracles General Scheme")

However, we get more variety with state oracles: State oracles are many atomic kinds depending on the particular type of state they manage. We can use this atomicity to combine the state oracles in many kinds of new decentralized services. E.g. state oracles managing physical delivery can be incorporated into e-commerce services.

Another advantage is that state oracles enable to unbind a function from its functionality. For instance, state oracles conducting a state transition of the same type can still use a different underlying technology for storage or consensus. Or from the other side: two state oracles can offer a different view of the same type of state.

# PoC

## Dapp
Dapp itself has not functionalities other that interpreting (rendering) state messages coming from State Oracles. Upcoming steps describe procedure of creating and submitting of Ethereum transaction with State Oracles.

## First step
When making an Ethereum payment, we need to fill out a form with payment details (address from/to, amount etc.) For this purpose, the dapp gets the html code of the form from “TransferProposalView” State Oracle.

![Step 1](/docs/images/eth-tx1.png?raw=true "Step 1")

## Second step
In the second step, the dapp obtains Ethereum raw transaction for intended token transfer. For this purpose, the dapp calls the UnsignedRawTransaction State Oracle with necessary attributes.

![Step 2](/docs/images/eth-tx2.png?raw=true "Step 2")

## Third step
In the third step, the dapp obtains and renders TransactionSigning View.

![Step 3](/docs/images/eth-tx3.png?raw=true "Step 3")

## Forth step
Finally the dapp submits the signed raw transaction to the State Oracle and gets a confirmation of the transaction in return.

![Step 4](/docs/images/eth-tx4.png?raw=true "Step 4")