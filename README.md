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

���E�@ul.pagination > li.total-page > span.total-page-num ��text_content()���� "1/577" ���擾��

�@�E�@ul.pagination > li.last-page > a ��get('href')��/spots�ȉ��̑���URL���擾��



----------------------------------------------------------


�e�v�f��Index�ɂ���

!!!�r���������Ă��邨���E�_�Ђ����邽�߁AIndex���؂ꂽ��IndexError�ł́A���ڂ�����邱�Ƃ�����!!!

�E�܂�func(spot_item)(div.spot_info_items > div.spot_item)�ɂ��ē��Ă͂܂�div�v�f��1~4�����o��

�E���̒����瓖�Ă͂܂���̂����Ԃɂ����Ă����A���ꂼ��A�������IndexError

-�@�Z���ihref������"https://www.google.com"�Ŏn�܂�a�v�f�j

�@��'a[href^="https://www.google.com"]'

 �A�d�b�ԍ��i�v�f�̎q����"-"�Ƃ����e�L�X�g���܂�div�v�f�j

�@��'div:contains("-")'
**********BUG**********
�E[�d�b�ԍ�]�̃g�s�b�N��URL�����ꍞ��ł��Ă���
��URL��"-"���܂ނ��̂�����


 �BURL�i�v�f�̎q����"http"�Ƃ����e�L�X�g���܂�a�v�f�j

�@��'a:contains("http")'

 �C����̗L���i�v�f�̎q����"-"�Ƃ����e�L�X�g���܂�div�v�f�j

�@��'div:contains("����")'



--------------------------------------------------------


��L�Ŏ�������ƁA�g�s�b�N�ɂ�荀�ڂ̃Y�������邽�߁AKeyError������

���o�͂�DB�ł͂Ȃ��A�ق��ɍl����

��csv�Ŏ����Aunique_kye�̂�DB:`omairi`, TABLE:`keys`�Ɋi�[

--------------------------------------------------------

��L�ł̎����̌��ʁAG��[�d�b�ԍ�]�ɁAH��[URL]�����ꍞ��ł���ӏ�������B
GitBranch:debug01�ł̏C���A����