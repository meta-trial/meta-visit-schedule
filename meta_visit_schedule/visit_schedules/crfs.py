from edc_visit_schedule import FormsCollection, Crf

crfs_prn = FormsCollection(
    Crf(show_order=1, model="meta_subject.bloodresult"),
    name="prn",
)

crfs_unscheduled = FormsCollection(
    Crf(show_order=1, model="meta_subject.bloodresult"), name="unscheduled"
)


crfs_d1 = FormsCollection(
    Crf(show_order=6, model="meta_subject.bloodresult"),
    name="day1",
)

crfs_3m = FormsCollection(
    Crf(show_order=1, model="meta_subject.bloodresult"), name="3m"
)

crfs_6m = FormsCollection(
    Crf(show_order=1, model="meta_subject.bloodresult"), name="6m"
)

crfs_9m = FormsCollection(
    Crf(show_order=1, model="meta_subject.bloodresult"),
    name="9m",
)

crfs_12m = FormsCollection(
    Crf(show_order=1, model="meta_subject.bloodresult"), name="12m"
)
