import numpy as np
import tulipy as ti

##
# Indicators
#


def srsi(values, rsi_length, stoch_length, k_period, d_period):
    rsi = ti.rsi(values, rsi_length)
    return ti.stoch(rsi, rsi, rsi, stoch_length, k_period, d_period)


def tsi(values, long_length, short_length, signal_length):
    change = np.diff(values)
    double_smoothed_change = double_smooth(change, long_length, short_length)
    double_smoothed_abs_change = double_smooth(abs(change), long_length, short_length)
    tsi_value = 100 * (double_smoothed_change / double_smoothed_abs_change)
    tsi_signal = ti.ema(tsi_value, signal_length)

    return tsi_value, tsi_signal


##
# Helpers
#


def double_smooth(values, long, short):
    first_smooth = ti.ema(values, long)
    return ti.ema(first_smooth, short)
