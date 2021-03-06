struct calibration_table {
  float ein;
  float coeff;
};
/* Quanta BMC correction table */
struct calibration_table power_table[] = {
  {68.76,   0.9961},
  {134.30,  0.9728},
  {199.03,  0.9681},
  {263.96,  0.9673},
  {329.32,  0.9641},
  {393.36,  0.9636},
  {459.47,  0.9621},
  {531.04,  0.9585},
  {597.94,  0.9619},
  {663.62,  0.9606},
  {728.49,  0.9609},
  {794.84,  0.9595},
  {859.47,  0.9603},
  {925.11,  0.9599},
  {990.08,  0.9592},
  {1055.52, 0.9589},
  {1121.40, 0.9575},
  {1185.35, 0.9582},
  {1250.36, 0.9578},
  {1315.56, 0.9576},
  {1379.58, 0.9574},
  {1445.56, 0.9575},
  {1510.73, 0.9567},
  {1573.77, 0.9570},
  {1639.11, 0.9554},
  {1693.72, 0.9596},
  {1758.04, 0.9571},
  {1819.52, 0.9577},
  {1879.58, 0.9589},
  {1936.22, 0.9613},
  {1988.46, 0.9631},
  {2041.03, 0.9644},
  {2101.97, 0.9636},
  {2164.33, 0.9652},
  {2221.34, 0.9677},
  {2281.01, 0.9683},
  {2334.58, 0.9699},
  {2392.10, 0.9704},
  {2448.41, 0.9736},
  {2508.02, 0.9733},
  {2561.48, 0.9756},
  {2633.89, 0.9740},
  {2685.56, 0.9753},
  {2734.88, 0.9790},
  {2795.28, 0.9780},
  {2853.37, 0.9781},
  {2911.23, 0.9783},
  {2963.27, 0.9803},
  {3024.88, 0.9795},
  {3082.33, 0.9810},
  {3148.96, 0.9811},
  {3220.39, 0.9826},
  {3287.83, 0.9798},
  {0.0,   0.0}
};

struct calibration_table current_table[] = {
  {5.65,   0.9870},
  {10.96,  0.9720},
  {16.23,  0.9684},
  {21.56,  0.9664},
  {26.60,  0.9744},
  {32.15,  0.9631},
  {37.45,  0.9623},
  {42.76,  0.9620},
  {48.07,  0.9624},
  {53.39,  0.9609},
  {58.69,  0.9607},
  {64.01,  0.9604},
  {69.32,  0.9601},
  {74.65,  0.9599},
  {79.96,  0.9595},
  {85.29,  0.9594},
  {90.63,  0.9587},
  {95.97,  0.9585},
  {101.29, 0.9583},
  {106.64, 0.9581},
  {111.97, 0.9574},
  {117.33, 0.9577},
  {122.70, 0.9570},
  {128.03, 0.9565},
  {133.30, 0.9567},
  {138.58, 0.9572},
  {143.78, 0.9578},
  {149.12, 0.9574},
  {154.28, 0.9584},
  {159.34, 0.9601},
  {164.37, 0.9616},
  {169.40, 0.9634},
  {174.39, 0.9649},
  {179.40, 0.9663},
  {184.40, 0.9676},
  {189.42, 0.9687},
  {194.42, 0.9697},
  {199.43, 0.9707},
  {204.29, 0.9730},
  {209.32, 0.9737},
  {214.26, 0.9749},
  {219.08, 0.9770},
  {224.26, 0.9769},
  {229.30, 0.9774},
  {232.64, 0.9850},
  {239.32, 0.9786},
  {244.35, 0.9790},
  {249.35, 0.9797},
  {254.34, 0.9803},
  {259.34, 0.9809},
  {264.36, 0.9816},
  {269.36, 0.9821},
  {274.34, 0.9826},
  {0.0,   0.0}
};

struct calibration_table aux_power_table[] = {
  {60.04,  1.0214},
  {96.42,  1.0099},
  {120.41, 1.0038},
  {156.49, 1.0053},
  {180.68, 1.0062},
  {215.92, 1.0085},
  {241.07, 1.0047},
  {276.62, 1.0066},
  {300.53, 1.0029},
  {337.23, 1.0039},
  {361.00, 1.0036},
  {396.49, 1.0034},
  {420.40, 1.0042},
  {456.74, 1.0045},
  {479.57, 1.0062},
  {503.58, 1.0048},
  {539.37, 1.0068},
  {0.0,   0.0}
};

struct calibration_table aux_current_table[] = {
  {4.96,  1.0234},
  {7.96,  1.0118},
  {9.96,  1.0053},
  {12.94, 1.0067},
  {14.96, 1.0076},
  {17.91, 1.0075},
  {19.98, 1.0044},
  {22.95, 1.0054},
  {24.96, 1.0008},
  {27.98, 1.0024},
  {29.98, 1.0017},
  {32.95, 1.0011},
  {34.94, 1.0019},
  {38.00, 1.0014},
  {39.92, 1.0026},
  {41.93, 1.0018},
  {44.96, 1.0022},
  {0.0,   0.0}
};
