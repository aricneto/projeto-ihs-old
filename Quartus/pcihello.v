
//=======================================================
//  This code is generated by Terasic System Builder
//=======================================================

module pcihello (

    //////////// CLOCK //////////
    CLOCK_50,  // BANK 4
    CLOCK2_50,  // BANK 7
    CLOCK3_50,  // BANK 3A

    //////////// LED (High Active) //////////
    LEDG,
    LEDR,

    //////////// KEY (Active Low) //////////
    KEY,

    // switches
    SW,

    //////////// SEG7 (Low Active) //////////
    HEX0,
    HEX1,
    HEX2,
    HEX3,
    HEX4,
    HEX5,
    HEX6,
    HEX7,

    //////////// PCIe //////////
    PCIE_PERST_N,
    PCIE_REFCLK_P,
    PCIE_RX_P,
    PCIE_TX_P,
    PCIE_WAKE_N,

    //////////// Fan Control //////////
    FAN_CTRL
);

  //=======================================================
  //  PARAMETER declarations
  //=======================================================


  //=======================================================
  //  PORT declarations
  //=======================================================

  //////////// CLOCK //////////
  input CLOCK_50;
  input CLOCK2_50;
  input CLOCK3_50;

  //////////// LED (High Active) //////////
  output [8:0] LEDG;
  output [17:0] LEDR;

  //////////// KEY (Active Low) //////////
  input [3:0] KEY;
  input [17:0] SW;

  //////////// SEG7 (Low Active) //////////
  output [6:0] HEX0;
  output [6:0] HEX1;
  output [6:0] HEX2;
  output [6:0] HEX3;
  output [6:0] HEX4;
  output [6:0] HEX5;
  output [6:0] HEX6;
  output [6:0] HEX7;

  //////////// PCIe //////////
  input PCIE_PERST_N;
  input PCIE_REFCLK_P;
  input [1:0] PCIE_RX_P;
  output [1:0] PCIE_TX_P;
  output PCIE_WAKE_N;

  //////////// Fan Control //////////
  inout FAN_CTRL;


  //=======================================================
  //  REG/WIRE declarations
  //=======================================================

  wire [31:0] hex_bus;
  wire [31:0] hex_bus2;

  wire [31:0] switches_bus;
  wire [31:0] push_buttons_bus;
  wire [31:0] led_red_bus;
  wire [31:0] led_grn_bus;
  wire        fan_bus;


  //=======================================================
  //  Structural coding
  //=======================================================

  pcihellocore u0 (
      .pcie_hard_ip_0_rx_in_rx_datain_0          (PCIE_RX_P[0]),
      .pcie_hard_ip_0_tx_out_tx_dataout_0        (PCIE_TX_P[0]),
      .pcie_hard_ip_0_powerdown_pll_powerdown    (PCIE_WAKE_N),
      .pcie_hard_ip_0_powerdown_gxb_powerdown    (PCIE_WAKE_N),
      .pcie_hard_ip_0_refclk_export              (PCIE_REFCLK_P),
      .pcie_hard_ip_0_pcie_rstn_export           (PCIE_PERST_N),
      .hex_display_external_connection_export    (hex_bus),
      .hex_display_2_external_connection_export  (hex_bus2),
      .switches_external_connection_export       (switches_bus),
      .push_buttons_external_connection_export   (push_buttons_bus),
      .red_leds_external_connection_export       (led_red_bus),
      .green_leds_external_connection_export     (led_grn_bus),
  );


  //////////// FAN Control //////////
  assign FAN_CTRL = 1'b1;  // turn on FAN

  // 7seg
  assign HEX0 = hex_bus[6:0];
  assign HEX1 = hex_bus[14:8];
  assign HEX2 = hex_bus[22:16];
  assign HEX3 = hex_bus[30:24];
  assign HEX4 = hex_bus2[6:0];
  assign HEX5 = hex_bus2[14:8];
  assign HEX6 = hex_bus2[22:16];
  assign HEX7 = hex_bus2[30:24];

  // leds
  assign LEDR = led_grn_bus[8:0];
  assign LEDG = led_red_bus[17:0];

  // switches
  assign switches_bus[15:0] = SW[15:0];

  // push buttons
  assign push_buttons_bus[3:0] = KEY;

endmodule
