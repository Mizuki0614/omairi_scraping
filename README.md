# omairi_scraping

�S���̐_�Е��t�̏���omairi.com����f�[�^���o���������B
�����������̂ŁAWEB�X�N���C�s���O�𐄏����܂��B


omairi.com��
[����]
[�Z��]
[���Аl�C�����L���O�i�s���{���j]
[���Аl�C�����L���O�i�S���j]
[�A�N�Z�X��]
[�ʐ^��]
[�d�b�ԍ�]
[URL]
[����̗L��]
[����ʐ^��URL]
�𒊏o����EXCEL���������B

--------------------------------------------------------

"�_�ЁE���������L���O(https://omairi.club/spots/ranking)"����A���ׂĂ�URL�̎擾
�`1�̃y�[�W���炨���E�_�ЌX��URL���擾�`
�Ediv.spot_ranking >a ��get('href')��/spot�ȉ��̑���URL���擾��
�E1�y�[�W������25���̂����v�E�_�Ђ�URL
�`���ׂẴy�[�W�̎擾�`
1�y�[�W�ځF�@https://omairi.club/spots/ranking
2�y�[�W�ځF�@https://omairi.club/spots/ranking/page/2
3�y�[�W�ځF�@https://omairi.club/spots/ranking/page/3
:
:
:
�Ō�̃y�[�W�̎擾
���E�@ul.pagination > li.total-page > span.total-page-num ��text_content()���� "1/1577" ���擾��
�@�E�@ul.pagination > li.last-page > a ��get('href')��/spots�ȉ��̑���URL���擾��