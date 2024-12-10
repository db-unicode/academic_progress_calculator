# Academic Progress Calculator

## Description

The Academic Progress Calculator is a Python-based software tool designed to analyze and compute a student's progress within a specified academic curriculum. By leveraging historical academic data, such as completed courses, grades, and credit requirements, this tool provides insightful metrics to help students, educators, and administrators evaluate academic standing and forecast graduation timelines.

## Installation

Follow these steps to install and set up the project:

1. Clone the repository:
    ```sh
    git clone <REPOSITORY_URL>
    cd <REPOSITORY_NAME>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```


## Configuration Summary

All configurations are managed through the `config.yml` file.

- **data_set_path**: This variable is used to specify the path to the CSV file containing historical academic data. The file must include specific headers for accurate processing.

- **report_until_date**: This variable defines the reporting cutoff date using the format `YYYYSM`, where `YYYY` is the year and `SM` specifies the semester (`10` for first semester, `20` for second semester).

- **curriculum_structure_path**: This variable indicates the path to a JSON file that describes the academic curriculum, including simple courses and course bundles with their details.

- **output_path**: This variable specifies the directory path where the generated reports will be saved.

- **student_codes**: This variable points to a JSON file containing a list of student codes to identify the students whose data will be processed.

- **report_name**: This variable is used as the prefix for the generated report filenames, which follow the format `{report_name}-{student_code}.json`.



##  Explanation of Variables in `config.yml`

### `data_set_path`
- **Type**: String
- **Description**: Specifies the path to the CSV file containing historical academic data. This file must include the following headers:
  - `CODIGO`, `PERIODO`, `MATERIA`, `DESCRIPCION_NIVEL_MATERIA`, `NUMERO_CREDITOS`, `DESCRIPCION_CAMPUS`, `ESTATUS_CURSO`, `DESCRIPCION_MODO_DE_CALIFICACION`, `CALIFICACION_PARCIAL`, `CALIFICACION_FINAL`, `SECCION`, `ATRIBUTO_CURSO`, `ATRIBUTO_SECCION`, `PARTE_PERIODO`, `NOMBRE_CURSO_EXAMEN`, `ESTADO_MATERIA`, `CODIGO_ASIGNATURA`, `NUMERO_CURSO`, `DESCRIPCION_ESTADO_MATERIA`, `DESCRIPCION_FACULTAD_CURSO`, `DESCRIPCION_DEPARTAMENTO_CURSO`, `CODIGO_NIVEL_PROGRAMA_1`, `NIVEL_PROGRAMA_1`, `DEPARTAMENTO_PROGRAMA_1`, `PROGRAMA_1`, `NIVEL_PROGRAMA_2`, `DEPARTAMENTO_PROGRAMA_2`, `PROGRAMA_2`, `NIVEL_PROGRAMA_3`, `DEPARTAMENTO_PROGRAMA_3`, `PROGRAMA_3`
- **Example**: `"src/data/research_data.csv"`

---

### `report_until_date`
- **Type**: String
- **Description**: Specifies the reporting cutoff date in the format `YYYYSM`. The `YYYY` represents the year, and `SM` represents the semester:
  - `10` for the first semester.
  - `20` for the second semester.
- **Example**: `"202520"` (Year 2025, second semester)

---

### `curriculum_structure_path`
- **Type**: String
- **Description**: Path to a JSON file defining the academic curriculum structure. The structure includes:
  - `simple_courses`: A list of objects where each course has:
    - `code`: The course code.
    - `name`: The course name.
  - `course_bundles`: A dictionary where each key represents a bundle, and its value contains:
    - `minimum_credits_to_pass`: Minimum credits required to pass this bundle.
    - `related_bundles`: A list of other related bundles (can be empty).
    - `courses`: A dictionary where each key is a course code, and the value is:
      - `type`: Course type (`OPTIONAL` or `REQUIRED`).
      - `name`: The course name.
- **Example**: `"src/curriculum_structures/sistemas.json"`

---

### `output_path`
- **Type**: String
- **Description**: Specifies the folder path where generated reports will be saved.
- **Example**: `"src/output"`

---

### `student_codes`
- **Type**: String
- **Description**: Path to a JSON file containing a list of student codes. These codes identify the students whose data will be processed and reported.
- **Example**: `"src/student_code_list/sistemas_student_code_list.json"`

---

### `report_name`
- **Type**: String
- **Description**: The prefix for the report filenames. The report for each student will follow the format `{report_name}-{student_code}.json`.
- **Example**: `"complete_report"`


## Usage

Once installed and configured, run the application with the following command:

```sh
python src/main.py
```
For each student code listed in the config.yml file, the application will generate a report in the specified output folder. Each report will be based on the selected curriculum structure defined in the config.yml file.