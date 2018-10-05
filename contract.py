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


class Contract(metaclass=PoolMeta):
    __name__ = 'contract'
    contact_address = fields.Many2One('party.address', 'Contact Address',
        domain=[('party', '=', Eval('party'))],
        states=_STATES, depends=_DEPENDS+['party'])

    @fields.depends('party')
    def on_change_party(self):
        super(Contract, self).on_change_party()

        self.contact_address = (self.party.addresses[0]
            if (self.party and self.party.addresses) else None)
