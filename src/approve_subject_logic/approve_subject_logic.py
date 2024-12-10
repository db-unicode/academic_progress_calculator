import pandas as pd


class ApproveSubjectLogic:
    @staticmethod
    def has_passed_subject(subject_df: pd.DataFrame) -> bool:
        """
        Determines if the student has passed or homologated the subject based on given DataFrame.
        
        :param subject_df: DataFrame containing records for a specific subject of a student.
        :return: True if the subject was passed or homologated, False otherwise.
        """
        # If the DataFrame is empty, the student hasn't taken the subject before the specified period
        if subject_df.empty:
            return False

        for _, row in subject_df.iterrows():
            course_status = row.get('ESTATUS_CURSO', None)
            grading_mode = row['DESCRIPCION_MODO_DE_CALIFICACION']
            final_grade = row['CALIFICACION_FINAL']
            
            # If the course was homologated, return True
            if course_status == 'HOMOLOGADO':
                return True

            # If the grading mode is not relevant, consider it as passed
            if grading_mode not in ['APROBADO/REPROBADO', 'ESTANDAR NUMERICO 1.5-5.0']:
                return True

            # If the grading mode is "APROBADO/REPROBADO"
            if grading_mode == 'APROBADO/REPROBADO':
                return final_grade == 'A'

            # If the grading mode is "ESTANDAR NUMERICO 1.5-5.0"
            if grading_mode == 'ESTANDAR NUMERICO 1.5-5.0':
                if final_grade == 'A':
                    return True
                try:
                    final_grade_float = float(final_grade)
                    return final_grade_float >= 3.0
                except ValueError:
                    # If final grade cannot be converted to float, consider it as failed
                    return False
        
        # If none of the conditions are met, return False
        return False
