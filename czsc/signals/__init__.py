# -*- coding: utf-8 -*-
"""
author: zengbin93
email: zeng_bin8888@163.com
create_dt: 2021/11/21 17:48
describe: 信号系统，注意：这里仅仅只是提供一些写信号的例子，用来做策略是不太行的
"""

from . import bxt

# ======================================================================================================================
# 以下是 0.9.1 开始的新标准下实现的信号函数，规范定义：
# 1. 前缀3个字符区分信号类别
# 2. 后缀 V221107 之类的标识同一个信号函数的不同版本
# ======================================================================================================================

from czsc.signals.cxt import (
    cxt_fx_power_V221107,
    cxt_first_buy_V221126,
    cxt_first_sell_V221126,
    cxt_zhong_shu_gong_zhen_V221221,
    cxt_bi_end_V230222,
    cxt_bi_end_V230224,
    cxt_bi_end_V230104,
    cxt_bi_end_V230105,
    cxt_bi_end_V230312,
    cxt_bi_end_V230320,
    cxt_bi_end_V230322,
    cxt_bi_end_V230324,
    cxt_bi_base_V230228,
    cxt_third_buy_V230228,
    cxt_double_zs_V230311,
    cxt_third_bs_V230318,
    cxt_third_bs_V230319,
    cxt_second_bs_V230320,
    cxt_bi_status_V230101,
    cxt_bi_status_V230102,
)


from czsc.signals.byi import (
    byi_symmetry_zs_V221107,
    byi_bi_end_V230106,
    byi_bi_end_V230107,
    byi_second_bs_V230324,
)

from czsc.signals.coo import (
    coo_td_V221110,
    coo_td_V221111,
)

from czsc.signals.vol import (
    vol_single_ma_V230214,
    vol_double_ma_V230214,
    vol_ti_suo_V221216,
    vol_gao_di_V221218,
)

from czsc.signals.bar import (
    bar_end_V221211,
    bar_operate_span_V221111,
    bar_zdt_V230331,
    bar_cross_ps_V221112,
    bar_section_momentum_V221112,
    bar_vol_grow_V221112,
    bar_mean_amount_V221112,
    bar_zdf_V221203,
    bar_accelerate_V221110,
    bar_accelerate_V221118,
    bar_fang_liang_break_V221216,
    bar_fake_break_V230204,
    bar_single_V230214,
    bar_amount_acc_V230214,
    bar_big_solid_V230215,
    bar_vol_bs1_V230224,
    bar_reversal_V230227,
    bar_bpm_V230227,
    bar_time_V230327,
    bar_weekday_V230328,
    bar_r_breaker_V230326,
    bar_dual_thrust_V230403,
    bar_single_V230506,
    bar_triple_V230506,
    bar_zt_count_V230504,
)

from czsc.signals.jcc import (
    jcc_san_xing_xian_V221023,
    jcc_ten_mo_V221028,
    jcc_san_fa_V20221115,
    jcc_san_fa_V20221118,
    jcc_wu_yun_gai_ding_V221101,
    jcc_ci_tou_V221101,
    jcc_xing_xian_V221118,
    jcc_fen_shou_xian_V20221113,
    jcc_yun_xian_V221118,
    jcc_zhu_huo_xian_V221027,
    jcc_ping_tou_V221113,
    jcc_zhuo_yao_dai_xian_v221113,
    jcc_two_crow_V221108,
    jcc_three_crow_V221108,
    jcc_szx_V221111,
    jcc_ta_xing_V221124,
    jcc_san_szx_V221122,
    jcc_shan_chun_V221121,
    jcc_fan_ji_xian_V221121,
    jcc_gap_yin_yang_V221121,
)


from czsc.signals.tas import (
    update_macd_cache,
    update_ma_cache,
    update_kdj_cache,
    update_boll_cache,
    update_rsi_cache,
    update_cci_cache,
    update_atr_cache,
    update_sar_cache,

    tas_macd_base_V221028,
    tas_macd_change_V221105,
    tas_macd_direct_V221106,
    tas_macd_power_V221108,
    tas_macd_xt_V221208,
    tas_macd_bc_V221201,
    tas_macd_first_bs_V221201,
    tas_macd_first_bs_V221216,
    tas_macd_second_bs_V221201,
    tas_macd_bs1_V230313,
    tas_macd_bs1_V230312,
    tas_macd_base_V230320,

    tas_ma_base_V221101,
    tas_ma_base_V221203,
    tas_ma_base_V230313,
    tas_ma_round_V221206,
    tas_double_ma_V221203,
    tas_double_ma_V230511,
    tas_ma_system_V230513,

    tas_boll_power_V221112,
    tas_boll_bc_V221118,
    tas_boll_vt_V230212,
    tas_boll_cc_V230312,

    tas_kdj_base_V221101,
    tas_kdj_evc_V221201,

    # tas_double_rsi_V221203,
    tas_rsi_base_V230227,

    tas_first_bs_V230217,
    tas_second_bs_V230228,
    tas_second_bs_V230303,

    tas_hlma_V230301,
    tas_cci_base_V230402,
    tas_kdj_evc_V230401,

    tas_atr_break_V230424,

    tas_sar_base_V230425,
)

from czsc.signals.pos import (
    pos_fx_stop_V230414,
    pos_ma_V230414,
    pos_holds_V230414,
    pos_bar_stop_V230524,
)


from czsc.signals.ang import (
    adtm_up_dw_line_V230603,
    amv_up_dw_line_V230603,
    asi_up_dw_line_V230603,
    clv_up_dw_line_V230605,
    cmo_up_dw_line_V230605,
)