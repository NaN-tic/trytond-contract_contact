# This file is part of the contract_contact module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .contract import *


def register():
    Pool.register(
        Contract,
        module='contract_contact', type_='model')
