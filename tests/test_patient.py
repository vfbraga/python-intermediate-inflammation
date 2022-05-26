"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name

def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Chandni'
    p = Doctor(name=name)

    assert p.name == name

def test_doctor_is_person():
    from inflammation.models import Doctor, Person
    p = Doctor(name='Chandni')

    assert isinstance(p, Person)

def test_patient_added_correctly():
    from inflammation.models import Doctor, Patient
    doc = Doctor(name='Chandni')
    p = Patient(name='Vittorio')

    doc.add_patient(p)

    assert doc.patients is not None
