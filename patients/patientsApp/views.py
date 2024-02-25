from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer
from sqlalchemy.orm import sessionmaker
from .models import Patient as SQLAlchemyPatient
from patients.settings import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

class PatientViewSet(viewsets.ViewSet):
    def list(self, request):
        session = Session()
        patients = session.query(SQLAlchemyPatient).all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            patient_data = serializer.validated_data
            patient = SQLAlchemyPatient(**patient_data)
            session = Session()
            session.add(patient)
            session.commit()

            patient = session.query(SQLAlchemyPatient).filter_by(**patient_data).first()
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, patientId=None):
        session = Session()
        patient = session.query(SQLAlchemyPatient).filter_by(id=patientId).first()
        if patient:
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        return Response({'message': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, patientId=None):
        session = Session()
        patient = session.query(SQLAlchemyPatient).filter_by(id=patientId).first()
        if patient:
            serializer = PatientSerializer(patient, data=request.data)
            if serializer.is_valid():
                patient_data = serializer.validated_data
                for key, value in patient_data.items():
                    setattr(patient, key, value)
                session.commit()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, patientId=None):
        session = Session()
        patient = session.query(SQLAlchemyPatient).filter_by(id=patientId).first()
        if patient:
            session.delete(patient)
            session.commit()
            return Response({'message': 'Patient deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)