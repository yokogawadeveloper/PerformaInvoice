# Generated by Django 3.2.7 on 2023-03-16 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orderAcknowledgement',
            fields=[
                ('OrderAckId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('RevNo', models.IntegerField(null=True)),
                ('Advance', models.FloatField(default=0.0, null=True)),
                ('Retention', models.FloatField(default=0.0, null=True)),
                ('MaterialReadinessDate', models.DateField(blank=True, null=True)),
                ('Freight', models.FloatField(default=0.0, null=True)),
                ('TotalAmount', models.FloatField(default=0.0, null=True)),
                ('SubmittedDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('DeleteFlag', models.BooleanField(null=True)),
                ('CategoryId', models.IntegerField(null=True)),
                ('DivisionId', models.IntegerField(null=True)),
                ('RegionId', models.IntegerField(null=True)),
                ('ProjectManagerId', models.IntegerField(null=True)),
                ('JobCode', models.CharField(max_length=50, null=True)),
                ('WBS', models.CharField(max_length=50, null=True)),
                ('Party_Address', models.CharField(max_length=50, null=True)),
                ('DeletedOn', models.DateTimeField(null=True)),
                ('TotalUnitPrice', models.FloatField(default=0.0, null=True)),
                ('TCSApplicable', models.CharField(max_length=50, null=True)),
                ('TCS', models.FloatField(default=0.0, null=True)),
                ('TCSAmount', models.FloatField(default=0.0, null=True)),
                ('TotalAmountWithTCS', models.FloatField(default=0.0, null=True)),
                ('GSTBaseValue', models.FloatField(default=0.0, null=True)),
                ('PI_DueDays', models.IntegerField(null=True)),
                ('PI_DueDate', models.DateField(null=True)),
                ('PI_Remarks', models.CharField(max_length=50, null=True)),
                ('PI_TotalDiscount', models.FloatField(default=0.0, null=True)),
                ('PI_TotalPf', models.FloatField(default=0.0, null=True)),
                ('PI_TotalFreight', models.FloatField(default=0.0, null=True)),
                ('PI_TotalSGST', models.FloatField(default=0.0, null=True)),
                ('PI_TotalCGST', models.FloatField(default=0.0, null=True)),
                ('PI_TotalIGST', models.FloatField(default=0.0, null=True)),
                ('PI_NO', models.IntegerField(null=True)),
                ('PI_CODE', models.CharField(max_length=100, null=True)),
                ('UpdatedDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_remarks', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='orderAcknowledgementHistory',
            fields=[
                ('OrderAck_HistoryId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ProformaItemid', models.IntegerField(null=True)),
                ('ProformaID', models.IntegerField(null=True)),
                ('Revno', models.IntegerField(null=True)),
                ('Type', models.CharField(max_length=50, null=True)),
                ('Description', models.CharField(max_length=1000, null=True)),
                ('PercentonAmt', models.CharField(max_length=1000, null=True)),
                ('APBGDetails', models.CharField(max_length=1000, null=True)),
                ('PartName', models.CharField(max_length=255, null=True)),
                ('HSN', models.CharField(max_length=50, null=True)),
                ('Qty', models.FloatField(blank=True, default=0.0, null=True)),
                ('UOM', models.CharField(max_length=50, null=True)),
                ('UnitPrice', models.FloatField(default=0.0, null=True)),
                ('Advance', models.FloatField(default=0.0, null=True)),
                ('Retention', models.FloatField(default=0.0, null=True)),
                ('MaterialReadinessDate', models.DateField(blank=True, null=True)),
                ('Freight', models.FloatField(default=0.0, null=True)),
                ('IGST', models.FloatField(default=0.0, null=True)),
                ('SGST', models.FloatField(default=0.0, null=True)),
                ('CGST', models.FloatField(default=0.0, null=True)),
                ('PaymentTerms', models.CharField(max_length=1000, null=True)),
                ('SubmittedDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('UpdatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeleteFlag', models.BooleanField(null=True)),
                ('category_id', models.IntegerField(null=True)),
                ('division_id', models.IntegerField(null=True)),
                ('region_id', models.IntegerField(null=True)),
                ('TotalAmount', models.FloatField(default=0.0, null=True)),
                ('TotalAdvance', models.FloatField(default=0.0, null=True)),
                ('TotalRetention', models.FloatField(default=0.0, null=True)),
                ('GSTBaseValue', models.FloatField(default=0.0, null=True)),
                ('PI_Qty', models.FloatField(blank=True, default=0.0, null=True)),
                ('PI_Discount', models.FloatField(default=0.0, null=True)),
                ('PI_Pf', models.FloatField(default=0.0, null=True)),
                ('PI_Freight', models.FloatField(default=0.0, null=True)),
                ('PI_SGST', models.FloatField(default=0.0, null=True)),
                ('PI_CGST', models.FloatField(default=0.0, null=True)),
                ('PI_IGST', models.FloatField(default=0.0, null=True)),
            ],
        ),
    ]
