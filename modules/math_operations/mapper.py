from modules.math_operations.operation_helper import *
# mapper saving function ref to a key (not called)
operation_mapper = {
    '+': apply_sum,
    '*': apply_mul,
    '**': apply_pow,
    '-': apply_sub,
    '/': apply_div
}
