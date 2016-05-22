# ������ 8. ������� 23
# ����������� ���� "���������" (��. �.������ ������������� �� Python. ��.4) ���, 
# ����� � ������� ����� ���������� ���������. ����� ������ �������� ����� �� ��������� � ��� ������, ���� � ���� ��� ������� �������������. 
# ������������ ������� ���������� �����, �� ������� �� ������, ���������� ����� ��� ���������, �������� ������ ���, ��� �������� ���������.

# Burmistrov V. D.
# 14.04.2016


import random

massiv_words = ["�������� ������", "������� ���� ����������", "���� �������� � �����", "������ ����� � �������", "�������� � �����������", "������ ���������", "��������������� ����"]

word = random.choice(massiv_words)

massiv = list(word.lower())

random.shuffle(massiv)

anagrm_word = ''.join(massiv)


print('�� �������� ���� �� ����� �����')
print('���� ��������', anagrm_word)


k = 100
user_word = ''

while user_word != word:
	k -= 10
	user_word = input('������� ����� >')
	
print('���������', word)
print('��������� � ���', k, '�����')