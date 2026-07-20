# 1-bit Full Adder

## What it does

This project implements a combinational 1-bit Full Adder.

### Inputs

| Pin | Function |
|-----|----------|
| ui[0] | A |
| ui[1] | B |
| ui[2] | Carry In (Cin) |

### Outputs

| Pin | Function |
|-----|----------|
| uo[0] | Sum |
| uo[1] | Carry Out (Cout) |

---

## How it works

The design implements the standard Boolean equations of a Full Adder.

### Sum

```
Sum = A XOR B XOR Cin
```

### Carry

```
Cout = (A AND B) OR (Cin AND (A XOR B))
```

Only the first two output pins are used.

All remaining outputs are tied to logic 0.

---

## How to test

Apply every combination of the three inputs.

| A | B | Cin | Sum | Carry |
|:-:|:-:|:-:|:-:|:-:|
|0|0|0|0|0|
|0|0|1|1|0|
|0|1|0|1|0|
|0|1|1|0|1|
|1|0|0|1|0|
|1|0|1|0|1|
|1|1|0|0|1|
|1|1|1|1|1|

The supplied Cocotb test automatically verifies all eight combinations.

---

## External hardware

No external hardware is required.
