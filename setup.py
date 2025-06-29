from setuptools import setup, find_packages

setup(
    name='ai_task_allocator',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='An AI-Driven Task Allocation system using Linear Programming',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ai-task-allocator',
    packages=find_packages(),
    install_requires=[
        'pulp==2.7.0',
        'pandas==2.2.2',
        'matplotlib==3.8.4',
        # Optional
        # 'streamlit==1.35.0',
        # 'seaborn==0.13.2',
        # 'openpyxl==3.1.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
