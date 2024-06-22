import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    unique_subject_counts = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    unique_subject_counts.columns = ['teacher_id', 'cnt']
    return unique_subject_counts