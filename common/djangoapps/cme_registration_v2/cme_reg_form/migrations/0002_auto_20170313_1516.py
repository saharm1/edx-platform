# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cme_reg_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrainfo',
            name='address_1',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='address_2',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='affiliation',
            field=models.CharField(blank=True, max_length=46, null=True, choices=[(b"Stanford Children's Health", b"Stanford Children's Health"), (b"Packard Children's Health Alliance (PCHA)", b"Packard Children's Health Alliance (PCHA)"), (b'Stanford Health Care', b'Stanford Health Care'), (b'Stanford University', b'Stanford University'), (b'University Healthcare Alliance (UHA)', b'University Healthcare Alliance (UHA)'), (b'Not affiliated with Stanford Medicine', b'Not affiliated with Stanford Medicine')]),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='birth_date',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='city',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'United States', b'United States'), (b'Afghanistan', b'Afghanistan'), (b'Aland Islands', b'Aland Islands'), (b'Albania', b'Albania'), (b'Algeria', b'Algeria'), (b'American Samoa', b'American Samoa'), (b'Andorra', b'Andorra'), (b'Angola', b'Angola'), (b'Anguilla', b'Anguilla'), (b'Antarctica', b'Antarctica'), (b'Antigua And Barbuda', b'Antigua And Barbuda'), (b'Argentina', b'Argentina'), (b'Armenia', b'Armenia'), (b'Aruba', b'Aruba'), (b'Australia', b'Australia'), (b'Austria', b'Austria'), (b'Azerbaijan', b'Azerbaijan'), (b'Bahamas', b'Bahamas'), (b'Bahrain', b'Bahrain'), (b'Bangladesh', b'Bangladesh'), (b'Barbados', b'Barbados'), (b'Belarus', b'Belarus'), (b'Belgium', b'Belgium'), (b'Belize', b'Belize'), (b'Benin', b'Benin'), (b'Bermuda', b'Bermuda'), (b'Bhutan', b'Bhutan'), (b'Bolivia', b'Bolivia'), (b'Bosnia And Herzegovina', b'Bosnia And Herzegovina'), (b'Botswana', b'Botswana'), (b'Bouvet Island', b'Bouvet Island'), (b'Brazil', b'Brazil'), (b'British Indian Ocean Territory', b'British Indian Ocean Territory'), (b'Brunei Darussalam', b'Brunei Darussalam'), (b'Bulgaria', b'Bulgaria'), (b'Burkina Faso', b'Burkina Faso'), (b'Burundi', b'Burundi'), (b'Cambodia', b'Cambodia'), (b'Cameroon', b'Cameroon'), (b'Canada', b'Canada'), (b'Cape Verde', b'Cape Verde'), (b'Cayman Islands', b'Cayman Islands'), (b'Central African Republic', b'Central African Republic'), (b'Chad', b'Chad'), (b'Chile', b'Chile'), (b'China', b'China'), (b'Christmas Island', b'Christmas Island'), (b'Cocos (Keeling) Islands', b'Cocos (Keeling) Islands'), (b'Colombia', b'Colombia'), (b'Comoros', b'Comoros'), (b'Congo', b'Congo'), (b'Congo, The Democratic Republic OfThe', b'Congo, The Democratic Republic OfThe'), (b'Cook Islands', b'Cook Islands'), (b'Costa Rica', b'Costa Rica'), (b"Cote D'lvoire", b"Cote D'lvoire"), (b'Croatia', b'Croatia'), (b'Cuba', b'Cuba'), (b'Cyprus', b'Cyprus'), (b'Czech Republic', b'Czech Republic'), (b'Denmark', b'Denmark'), (b'Djibouti', b'Djibouti'), (b'Dominica', b'Dominica'), (b'Dominican Republic', b'Dominican Republic'), (b'Ecuador', b'Ecuador'), (b'Egypt', b'Egypt'), (b'El Salvador', b'El Salvador'), (b'Equatorial Guinea', b'Equatorial Guinea'), (b'Eritrea', b'Eritrea'), (b'Estonia', b'Estonia'), (b'Ethiopia', b'Ethiopia'), (b'Falkland Islands (Malvinas)', b'Falkland Islands (Malvinas)'), (b'Faroe Islands', b'Faroe Islands'), (b'Fiji', b'Fiji'), (b'Finland', b'Finland'), (b'France', b'France'), (b'French Guiana', b'French Guiana'), (b'French Polynesia', b'French Polynesia'), (b'French Southern Territories', b'French Southern Territories'), (b'Gabon', b'Gabon'), (b'Gambia', b'Gambia'), (b'Georgia', b'Georgia'), (b'Germany', b'Germany'), (b'Ghana', b'Ghana'), (b'Gibraltar', b'Gibraltar'), (b'Greece', b'Greece'), (b'Greenland', b'Greenland'), (b'Grenada', b'Grenada'), (b'Guadeloupe', b'Guadeloupe'), (b'Guam', b'Guam'), (b'Guatemala', b'Guatemala'), (b'Guernsey', b'Guernsey'), (b'Guinea', b'Guinea'), (b'Guinea-Bissau', b'Guinea-Bissau'), (b'Guyana', b'Guyana'), (b'Haiti', b'Haiti'), (b'Heard Island And McDonald Is lands', b'Heard Island And McDonald Is lands'), (b'Holy See (Vatican City State)', b'Holy See (Vatican City State)'), (b'Honduras', b'Honduras'), (b'Hong Kong', b'Hong Kong'), (b'Hungary', b'Hungary'), (b'Iceland', b'Iceland'), (b'India', b'India'), (b'Indonesia', b'Indonesia'), (b'Iran, Islamic Republic Of', b'Iran, Islamic Republic Of'), (b'Iraq', b'Iraq'), (b'Ireland', b'Ireland'), (b'Isle Of Man', b'Isle Of Man'), (b'Israel', b'Israel'), (b'Italy', b'Italy'), (b'Jamaica', b'Jamaica'), (b'Japan', b'Japan'), (b'Jersey', b'Jersey'), (b'Jordan', b'Jordan'), (b'Kazakhstan', b'Kazakhstan'), (b'Kenya', b'Kenya'), (b'Kiribati', b'Kiribati'), (b"Korea, Democratic People's Republic Of", b"Korea, Democratic People's Republic Of"), (b'Korea, Republic Of', b'Korea, Republic Of'), (b'Kuwait', b'Kuwait'), (b'Kyrgyzstan', b'Kyrgyzstan'), (b"Lao People's Democratic Republic", b"Lao People's Democratic Republic"), (b'Latvia', b'Latvia'), (b'Lebanon', b'Lebanon'), (b'Lesotho', b'Lesotho'), (b'Liberia', b'Liberia'), (b'Libyan Arab Jamahiriya', b'Libyan Arab Jamahiriya'), (b'Liechtenstein', b'Liechtenstein'), (b'Lithuania', b'Lithuania'), (b'Luxembourg', b'Luxembourg'), (b'Macao', b'Macao'), (b'Macedonia, The Former Yugoslav Republic Of', b'Macedonia, The Former Yugoslav Republic Of'), (b'Madagascar', b'Madagascar'), (b'Malawi', b'Malawi'), (b'Malaysia', b'Malaysia'), (b'Maldives', b'Maldives'), (b'Mali', b'Mali'), (b'Malta', b'Malta'), (b'Marshall Islands', b'Marshall Islands'), (b'Martinique', b'Martinique'), (b'Mauritania', b'Mauritania'), (b'Mauritius', b'Mauritius'), (b'Mayotte', b'Mayotte'), (b'Mexico', b'Mexico'), (b'Micronesia, Federated States Of', b'Micronesia, Federated States Of'), (b'Moldova, Republic Of', b'Moldova, Republic Of'), (b'Monaco', b'Monaco'), (b'Mongolia', b'Mongolia'), (b'Montenegro', b'Montenegro'), (b'Montserrat', b'Montserrat'), (b'Morocco', b'Morocco'), (b'Mozambique', b'Mozambique'), (b'Myanmar', b'Myanmar'), (b'Namibia', b'Namibia'), (b'Nauru', b'Nauru'), (b'Nepal', b'Nepal'), (b'Netherlands', b'Netherlands'), (b'Netherlands Antilles', b'Netherlands Antilles'), (b'New Caledonia', b'New Caledonia'), (b'New Zealand', b'New Zealand'), (b'Nicaragua', b'Nicaragua'), (b'Niger', b'Niger'), (b'Nigeria', b'Nigeria'), (b'Niue', b'Niue'), (b'Norfolk Island', b'Norfolk Island'), (b'Northern Mariana Islands', b'Northern Mariana Islands'), (b'Norway', b'Norway'), (b'Oman', b'Oman'), (b'Pakistan', b'Pakistan'), (b'Palau', b'Palau'), (b'Palestinian Territory, Occupied', b'Palestinian Territory, Occupied'), (b'Panama', b'Panama'), (b'Papua New Guinea', b'Papua New Guinea'), (b'Paraguay', b'Paraguay'), (b'Peru', b'Peru'), (b'Philippines', b'Philippines'), (b'Pitcairn', b'Pitcairn'), (b'Poland', b'Poland'), (b'Portugal', b'Portugal'), (b'Puerto Rico', b'Puerto Rico'), (b'Qatar', b'Qatar'), (b'Reunion', b'Reunion'), (b'Romania', b'Romania'), (b'Russia', b'Russia'), (b'Rwanda', b'Rwanda'), (b'Saint Helena', b'Saint Helena'), (b'Saint Kitts And Nevis', b'Saint Kitts And Nevis'), (b'Saint Lucia', b'Saint Lucia'), (b'Saint Pierre And Miquelon', b'Saint Pierre And Miquelon'), (b'Saint Vincent And The Grenadines', b'Saint Vincent And The Grenadines'), (b'Samoa', b'Samoa'), (b'San Marino', b'San Marino'), (b'Sao Tome And Principe', b'Sao Tome And Principe'), (b'Saudi Arabia', b'Saudi Arabia'), (b'Senegal', b'Senegal'), (b'Serbia', b'Serbia'), (b'Seychelles', b'Seychelles'), (b'Sierra Leone', b'Sierra Leone'), (b'Singapore', b'Singapore'), (b'Slovakia', b'Slovakia'), (b'Slovenia', b'Slovenia'), (b'Solomon Islands', b'Solomon Islands'), (b'Somalia', b'Somalia'), (b'South Africa', b'South Africa'), (b'South Georgia And The South Sandwich Islands', b'South Georgia And The South Sandwich Islands'), (b'South Sudan', b'South Sudan'), (b'Spain', b'Spain'), (b'Sri Lanka', b'Sri Lanka'), (b'Sudan', b'Sudan'), (b'Suriname', b'Suriname'), (b'Svalbard And Jan Mayen', b'Svalbard And Jan Mayen'), (b'Swaziland', b'Swaziland'), (b'Sweden', b'Sweden'), (b'Switzerland', b'Switzerland'), (b'Syrian Arab Republic', b'Syrian Arab Republic'), (b'Taiwan', b'Taiwan'), (b'Tajikistan', b'Tajikistan'), (b'Tanzania, United Republic Of', b'Tanzania, United Republic Of'), (b'Thailand', b'Thailand'), (b'Timor-Leste', b'Timor-Leste'), (b'Togo', b'Togo'), (b'Tokelau', b'Tokelau'), (b'Tonga', b'Tonga'), (b'Trinidad And Tobago', b'Trinidad And Tobago'), (b'Tunisia', b'Tunisia'), (b'Turkey', b'Turkey'), (b'Turkmenistan', b'Turkmenistan'), (b'Turks And Caicos Islands', b'Turks And Caicos Islands'), (b'Tuvalu', b'Tuvalu'), (b'U.S. Minor Outlying Islands', b'U.S. Minor Outlying Islands'), (b'Uganda', b'Uganda'), (b'Ukraine', b'Ukraine'), (b'United Arab Emirates', b'United Arab Emirates'), (b'United Kingdom', b'United Kingdom'), (b'Uruguay', b'Uruguay'), (b'Uzbekistan', b'Uzbekistan'), (b'Vanuatu', b'Vanuatu'), (b'Venezuela', b'Venezuela'), (b'Viet Nam', b'Viet Nam'), (b'Virgin Islands, British', b'Virgin Islands, British'), (b'Virgin Islands, U.S.', b'Virgin Islands, U.S.'), (b'Wallis And Futuna', b'Wallis And Futuna'), (b'Western Sahara', b'Western Sahara'), (b'Yemen', b'Yemen'), (b'Zambia', b'Zambia'), (b'Zimbabwe', b'Zimbabwe'), (b'Other', b'Other')]),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='county_province',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='first_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='last_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='license_country',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='license_number',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='license_state',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='middle_initial',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='other_affiliation',
            field=models.CharField(max_length=46, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='patient_population',
            field=models.CharField(blank=True, max_length=25, null=True, choices=[(b'Adult', b'Adult'), (b'Pediatric', b'Pediatric'), (b'Both', b'Both'), (b'None', b'None')]),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='physician_status',
            field=models.CharField(blank=True, max_length=8, null=True, choices=[(b'Active', b'Active'), (b'Resident', b'Resident'), (b'Fellow', b'Fellow'), (b'Retired', b'Retired')]),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='postal_code',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='professional_designation',
            field=models.CharField(blank=True, max_length=25, null=True, choices=[(b'AuD', b'AuD'), (b'DDS', b'DDS'), (b'DO', b'DO'), (b'MD', b'MD'), (b'MD,PhD', b'MD,PhD'), (b'MBBS', b'MBBS'), (b'NP', b'NP'), (b'PA', b'PA'), (b'PharmD', b'PharmD'), (b'PhD', b'PhD'), (b'RN', b'RN'), (b'Other', b'Other'), (b'None', b'None')]),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='specialty',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Allergy,_Immunology,_&_Rheumatology', b'Allergy, Immunology, & Rheumatology'), (b'Anesthesiology', b'Anesthesiology'), (b'Cardiovascular_Health', b'Cardiovascular Health'), (b'Complimentary_Medicine_&_Pain_Management', b'Complimentary Medicine & Pain Management'), (b'Critical_Care_&_Pulmonology', b'Critical Care & Pulmonology'), (b'Dental_Specialties', b'Dental Specialties'), (b'Dermatology', b'Dermatology'), (b'Emergency_Medicine_&_Trauma', b'Emergency Medicine & Trauma'), (b'Endocrinology_&_Metabolism', b'Endocrinology & Metabolism'), (b'Family_Medicine_&_Community_Health', b'Family Medicine & Community Health'), (b'Gastroenterology_&_Hepatology', b'Gastroenterology & Hepatology'), (b'Genetics_&_Genomics', b'Genetics & Genomics'), (b'Gerontology', b'Gerontology'), (b'Hematology', b'Hematology'), (b'Infectious_Disease_&_Global_Health', b'Infectious Disease & Global Health'), (b'Internal_Medicine', b'Internal Medicine'), (b'Nephrology', b'Nephrology'), (b'Neurology_&_Neurologic_Surgery', b'Neurology & Neurologic Surgery'), (b'Obstetrics_&_Gynecology', b'Obstetrics & Gynecology'), (b'Oncology', b'Oncology'), (b'Ophthalmology', b'Ophthalmology'), (b'Orthopedics_&_Sports_Medicine', b'Orthopedics & Sports Medicine'), (b'Otolaryngology_(ENT)', b'Otolaryngology (ENT)'), (b'Pathology_&_Laboratory_Medicine', b'Pathology & Laboratory Medicine'), (b'Pediatrics', b'Pediatrics'), (b'Preventative_Medicine_&_Nutrition', b'Preventative Medicine & Nutrition'), (b'Psychiatry_&_Behavioral_Sciences', b'Psychiatry & Behavioral Sciences'), (b'Radiology', b'Radiology'), (b'Surgery', b'Surgery'), (b'Urology', b'Urology'), (b'Other/None', b'Other/None')]),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='stanford_department',
            field=models.CharField(blank=True, max_length=46, null=True, choices=[(b'Anesthesiology,Perioperative,Pain Medicine', b'Anesthesiology,Perioperative,Pain Medicine'), (b'Biochemistry', b'Biochemistry'), (b'Cardiothoracic Surgery', b'Cardiothoracic Surgery'), (b'Centers - School of Medicine', b'Centers - School of Medicine'), (b'Chemical and Systems Biology', b'Chemical and Systems Biology'), (b'Comparative Medicine', b'Comparative Medicine'), (b'Dermatology', b'Dermatology'), (b'Developmental Biology', b'Developmental Biology'), (b'Genetics Operations', b'Genetics Operations'), (b'Health Research and Policy', b'Health Research and Policy'), (b'Medicine', b'Medicine'), (b'Microbiology and Immunology', b'Microbiology and Immunology'), (b'Molecular and Cellular Physiology', b'Molecular and Cellular Physiology'), (b'Neurobiology', b'Neurobiology'), (b'Neurology', b'Neurology'), (b'Neurosurgery', b'Neurosurgery'), (b'Obstetrics & Gynecology', b'Obstetrics & Gynecology'), (b'Ophthalmology', b'Ophthalmology'), (b'Orthopaedic Surgery', b'Orthopaedic Surgery'), (b'Otolaryngology/Head & Neck Surgery', b'Otolaryngology/Head & Neck Surgery'), (b'Pathology', b'Pathology'), (b'Pediatrics', b'Pediatrics'), (b'Psychiatry and Behavioral Sciences', b'Psychiatry and Behavioral Sciences'), (b'Radiation Oncology', b'Radiation Oncology'), (b'Radiology', b'Radiology'), (b'School of Medicine', b'School of Medicine'), (b'SoM - Basic Science Pool', b'SoM - Basic Science Pool'), (b'SoM - Bio-X/Clark', b'SoM - Bio-X/Clark'), (b'SoM - Bioengineering', b'SoM - Bioengineering'), (b'SoM - Clinical Science Pool', b'SoM - Clinical Science Pool'), (b'SoM - Other Departments', b'SoM - Other Departments'), (b"SoM Dean's Office Administrative Units", b"SoM Dean's Office Administrative Units"), (b'SoM Non Cap Projects', b'SoM Non Cap Projects'), (b'Stanford Cancer/Stem Cell Biology', b'Stanford Cancer/Stem Cell Biology'), (b'Stanford Institutes of Medicine', b'Stanford Institutes of Medicine'), (b'Structural Biology Department', b'Structural Biology Department'), (b'Surgery', b'Surgery'), (b'Urology', b'Urology'), (b'Urology - Administration', b'Urology - Administration'), (b'Urology - Divisions', b'Urology - Divisions')]),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Deleware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')]),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='sub_affiliation',
            field=models.CharField(max_length=46, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='sub_specialty',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='sunet_id',
            field=models.CharField(max_length=33, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='favorite_movie',
            field=models.CharField(max_length=100, verbose_name=b'Fav Flick'),
        ),
    ]
