`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IO inputs
    output wire [7:0] uio_out,  // IO outputs
    output wire [7:0] uio_oe,   // IO output enable
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    //=============================
    // Input Assignment
    //=============================
    wire A   = ui_in[0];
    wire B   = ui_in[1];
    wire Cin = ui_in[2];

    //=============================
    // Full Adder Logic
    //=============================
    wire Sum;
    wire Cout;

    assign Sum  = A ^ B ^ Cin;
    assign Cout = (A & B) | (Cin & (A ^ B));

    //=============================
    // Output Assignment
    //=============================
    assign uo_out[0] = Sum;
    assign uo_out[1] = Cout;

    // Các chân còn lại xuất 0
    assign uo_out[7:2] = 6'b000000;

    // Không sử dụng IO mở rộng
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Tránh warning
    wire _unused = &{ena, clk, rst_n, uio_in};

endmodule
