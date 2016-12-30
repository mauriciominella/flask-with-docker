FROM python:3.4-onbuild 
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["app.py"]
