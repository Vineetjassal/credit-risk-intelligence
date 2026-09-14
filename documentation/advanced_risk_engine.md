# Advanced Risk Engine

CreditWatch now includes a transparent analytical layer for **PD × LGD × EAD** and rating migration.

## Expected Loss

`Expected Loss = PD × LGD × EAD`

- **PD**: probability of distress/default proxy.
- **LGD**: loss severity after recoveries/collateral.
- **EAD**: expected exposure at the event date.

The implementation also exposes an unexpected-loss proxy for portfolio analytics. It is deliberately labelled a prototype and is not a regulatory capital calculation.

## LGD

LGD can be supplied directly from a recovery assumption, or estimated from collateral coverage using a transparent capped recovery heuristic. Production use should replace this with validated workout/recovery data.

## EAD

`EAD = current exposure + CCF × undrawn limit`

The credit-conversion factor is bounded between 0 and 100%.

## Rating Migration

The prototype rating scale is `AAA → AA → A → BBB → BB → B → CCC → CC → C → D`. The engine provides one-notch upgrade and downgrade states around the current rating. A production transition matrix should be estimated from historical migrations and validated by rating grade, sector and time horizon.

## Governance

All outputs are intended for analytical demonstration. No synthetic output should be represented as an actual borrower default probability, regulatory capital requirement, or investment recommendation without validated data, model governance, and appropriate approvals.
