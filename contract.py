# This file is part of the contract_contact module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval


__all__ = ['Contract']
_STATES = {
    'readonly': Eval('state') != 'draft',
}
_DEPENDS = ['state']


class Contract:
    __metaclass__ = PoolMeta
    __name__ = 'contract'
    contact_address = fields.Many2One('party.address', 'Contact Address',
        states=_STATES, depends=['state', 'party'],
        domain=[('party', '=', Eval('party'))])

    def on_change_party(self):
        try:
            super(Contract, self).on_change_party()
        except AttributeError:
            pass

        self.contact_address = None
        if self.party:
            contact_address = self.party.address_get(type='contact')
            if contact_address:
                self.contact_address = contact_address
