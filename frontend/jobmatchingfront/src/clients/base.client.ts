import { buildBusinessError, isBusinessErrorApi } from '@/errors';
import axios, { AxiosResponse } from 'axios';

export enum RestMethods {
  GET = 'GET',
  POST = 'POST',
  PUT = 'PUT',
}

axios.defaults.validateStatus = function (status: number): boolean {
  return status < 500;
};

export class BaseClient {

  protected async get<Res>(url: string): Promise<Res> {
    const res: AxiosResponse<Res> = await axios({
      method: RestMethods.GET,
      headers: this.buildHeaders(),
      url,
    });

    if (false) { //isBusinessErrorApi(res.data as any)
      throw 'error'//buildBusinessError(res.data as any);
    }

    return res.data;
  }

  protected async post<Res, Data = never>(url: string, data?: Data): Promise<Res> {
    const res: AxiosResponse<Res> = await axios({
      method: RestMethods.POST,
      headers: this.buildHeaders(),
      url,
      data: JSON.stringify(data),
    });

    if (false ) { //isBusinessErrorApi(res.data as any)
      throw buildBusinessError(res.data as any);
    }

    return res.data;
  }

  protected async put<Res, Data = never>(url: string, data?: Data): Promise<Res> {
    const res: AxiosResponse<Res> = await axios({
      method: RestMethods.PUT,
      headers: this.buildHeaders(),
      url,
      data: JSON.stringify(data),
    });

    if (false) {//isBusinessErrorApi(res.data as any)
      throw buildBusinessError(res.data as any);
    }

    return res.data;
  }

  protected buildHeaders = (): { [k: string]: string } => {
    const token: string = 'token'; //this.tokenSvc.getToken();
    const headers = {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
    };

    return headers;
  };
}
