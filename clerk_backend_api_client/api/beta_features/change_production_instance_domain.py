from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_production_instance_domain_body import ChangeProductionInstanceDomainBody
from ...types import Response


def _get_kwargs(
    *,
    body: ChangeProductionInstanceDomainBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/instance/change_domain",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.ACCEPTED:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChangeProductionInstanceDomainBody,
) -> Response[Any]:
    """Update production instance domain

     Change the domain of a production instance.

    Changing the domain requires updating the [DNS
    records](https://clerk.com/docs/deployments/overview#dns-records) accordingly, deploying new [SSL
    certificates](https://clerk.com/docs/deployments/overview#deploy), updating your Social Connection's
    redirect URLs and setting the new keys in your code.

    WARNING: Changing your domain will invalidate all current user sessions (i.e. users will be logged
    out). Also, while your application is being deployed, a small downtime is expected to occur.

    Args:
        body (ChangeProductionInstanceDomainBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChangeProductionInstanceDomainBody,
) -> Response[Any]:
    """Update production instance domain

     Change the domain of a production instance.

    Changing the domain requires updating the [DNS
    records](https://clerk.com/docs/deployments/overview#dns-records) accordingly, deploying new [SSL
    certificates](https://clerk.com/docs/deployments/overview#deploy), updating your Social Connection's
    redirect URLs and setting the new keys in your code.

    WARNING: Changing your domain will invalidate all current user sessions (i.e. users will be logged
    out). Also, while your application is being deployed, a small downtime is expected to occur.

    Args:
        body (ChangeProductionInstanceDomainBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
