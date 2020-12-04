# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import opportunity

def register():
    Pool.register(
        opportunity.Priority,
        opportunity.Opportunity,
        module='sale_opportunity_priority', type_='model')
