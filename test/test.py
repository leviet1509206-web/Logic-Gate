# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_full_adder(dut):

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.uio_in.value = 0

    # Reset
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 5)

    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    truth_table = [
        (0,0,0,0,0),
        (0,0,1,1,0),
        (0,1,0,1,0),
        (0,1,1,0,1),
        (1,0,0,1,0),
        (1,0,1,0,1),
        (1,1,0,0,1),
        (1,1,1,1,1),
    ]

    for A,B,Cin,Sum,Cout in truth_table:

        dut.ui_in.value = (Cin<<2) | (B<<1) | A

        await ClockCycles(dut.clk,1)

        actual_sum = int(dut.uo_out.value) & 1
        actual_cout = (int(dut.uo_out.value)>>1)&1

        dut._log.info(
            f"A={A} B={B} Cin={Cin} -> "
            f"Sum={actual_sum} Cout={actual_cout}"
        )

        assert actual_sum == Sum
        assert actual_cout == Cout
