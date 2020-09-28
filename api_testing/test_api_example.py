import pytest
import random


@pytest.mark.parametrize("input_id", "output_id", [(10000, '10000'), (-1, '-1'), (0, '0')])
@pytest.mark.parametrize("input_title", "output_title", [('title', 'title'), ('', ''), (100, '100')])
def test_api_post_request(api_client, input_id, output_id, input_title, output_title):
    res = api_client.post(
        path="/posts",
        data={
            'title': input_title,
            'body': 'bar',
            'user_id': input_id,
        }).json()

    assert res['title'] == output_title
    assert res['body'] == 'bar'
    assert res['userId'] == output_id

