from meta_labs import fbc_panel
from meta_sites import meta_sites
from edc_visit_schedule import FormsCollection, Requisition


requisitions_prn = FormsCollection(
    Requisition(show_order=10, panel=fbc_panel,
                required=True, additional=False),
    name="requisitions_prn",
)

requisitions_d1 = FormsCollection(
    Requisition(show_order=10, panel=fbc_panel,
                required=True, additional=False),
    name="requisitions_day1",
)

requisitions_m3 = FormsCollection(
    Requisition(show_order=10, panel=fbc_panel,
                required=True, additional=False),
    name="requisitions_month3",
)

requisitions_m6 = FormsCollection(
    Requisition(show_order=10, panel=fbc_panel,
                required=True, additional=False),
    name="requisitions_default",
)

requisitions_m9 = FormsCollection(
    Requisition(show_order=10, panel=fbc_panel,
                required=True, additional=False),
    name="requisitions_month97",
)

requisitions_m12 = FormsCollection(
    Requisition(show_order=10, panel=fbc_panel,
                required=True, additional=False),
    name="requisitions_month12",
)
